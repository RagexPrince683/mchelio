package mcheli.aircraft;

import mcheli.MCH_Config;

/**
 * Vehicle-level cache for calculated extra bounding boxes.
 *
 * This is the behavior-preserving foundation for future rotating/oriented
 * vehicle collision boxes.  The cached boxes are still the existing
 * AxisAlignedBB-backed MCH_BoundingBox instances; this class only centralizes
 * when those boxes are recalculated so stationary vehicles can reuse them.
 */
public class MCH_VehicleBoxCache {
    private static final double POSITION_EPSILON = 1.0E-5D;
    private static final float ROTATION_EPSILON = 1.0E-4F;

    private boolean valid;
    private double posX;
    private double posY;
    private double posZ;
    private float yaw;
    private float pitch;
    private float roll;
    private String typeName;
    private MCH_BaseVehicleInfo info;
    private MCH_BoundingBox[] sourceBoxes;
    private int sourceBoxCount;
    private int mountedEntityCount;
    private int lastUpdateTick;
    private String dirtyReason = "new cache";

    /**
     * Returns the current world-space vehicle extra boxes, rebuilding them only
     * when transform/config/source state changed beyond the cache epsilons.
     */
    public MCH_BoundingBox[] getCalculatedBoxes(MCH_EntityBaseVehicle vehicle) {
        MCH_BoundingBox[] boxes = vehicle.extraBoundingBox;
        if (boxes == null) {
            invalidate("source boxes are null");
            return null;
        }

        String reason = getInvalidReason(vehicle, boxes);
        if (reason != null) {
            rebuild(vehicle, boxes, reason);
        } else {
            this.lastUpdateTick = vehicle.field_70173_aa;
            debug(vehicle, "hit", null, boxes.length);
        }
        return boxes;
    }

    public void invalidate(String reason) {
        this.valid = false;
        this.dirtyReason = reason;
    }

    private String getInvalidReason(MCH_EntityBaseVehicle vehicle, MCH_BoundingBox[] boxes) {
        if (!this.valid) return this.dirtyReason;
        if (this.sourceBoxes != boxes) return "source box array changed";
        if (this.sourceBoxCount != boxes.length) return "source box count changed";
        if (this.info != vehicle.getAcInfo()) return "vehicle config changed";

        String currentTypeName = vehicle.getTypeName();
        if (this.typeName == null ? currentTypeName != null : !this.typeName.equals(currentTypeName)) return "vehicle type changed";
        if (Math.abs(this.posX - vehicle.field_70165_t) > POSITION_EPSILON || Math.abs(this.posY - vehicle.field_70163_u) > POSITION_EPSILON || Math.abs(this.posZ - vehicle.field_70161_v) > POSITION_EPSILON) return "position changed";
        if (Math.abs(this.yaw - vehicle.getRotYaw()) > ROTATION_EPSILON || Math.abs(this.pitch - vehicle.getRotPitch()) > ROTATION_EPSILON || Math.abs(this.roll - vehicle.getRotRoll()) > ROTATION_EPSILON) return "rotation changed";
        if (this.mountedEntityCount != vehicle.getMountedEntityNum()) return "mounted entity count changed";
        return null;
    }

    private void rebuild(MCH_EntityBaseVehicle vehicle, MCH_BoundingBox[] boxes, String reason) {
        this.posX = vehicle.field_70165_t;
        this.posY = vehicle.field_70163_u;
        this.posZ = vehicle.field_70161_v;
        this.yaw = vehicle.getRotYaw();
        this.pitch = vehicle.getRotPitch();
        this.roll = vehicle.getRotRoll();
        this.typeName = vehicle.getTypeName();
        this.info = vehicle.getAcInfo();
        this.sourceBoxes = boxes;
        this.sourceBoxCount = boxes.length;
        this.mountedEntityCount = vehicle.getMountedEntityNum();
        this.lastUpdateTick = vehicle.field_70173_aa;
        this.valid = true;
        this.dirtyReason = null;

        for (int i = 0; i < boxes.length; ++i) {
            boxes[i].updatePosition(this.posX, this.posY, this.posZ, this.yaw, this.pitch, this.roll);
        }
        debug(vehicle, "rebuild", reason, boxes.length);
    }

    private static void debug(MCH_EntityBaseVehicle vehicle, String action, String reason, int count) {
        if (!isDebugEnabled()) return;
        System.out.println("[MCHeli][VehicleBoxCache] " + action + " vehicle=" + vehicle.getTypeName() + " boxes=" + count + (reason != null ? " reason=" + reason : ""));
    }

    private static boolean isDebugEnabled() {
        return Boolean.getBoolean("mcheli.debugVehicleBoxCache") || MCH_Config.DebugLog;
    }
}
