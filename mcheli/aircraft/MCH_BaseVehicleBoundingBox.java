package mcheli.aircraft;

import mcheli.ship.MCH_EntityShip;
import net.minecraft.util.AxisAlignedBB;
import net.minecraft.util.MovingObjectPosition;
import net.minecraft.util.Vec3;

/**
 * Vehicle bounding box wrapper that also queries vehicle extra hit/collision
 * boxes through MCH_VehicleBoxCache.  The cache intentionally preserves the
 * current AxisAlignedBB behavior while providing a single boundary where future
 * oriented/rotating vehicle box math can be implemented.
 */
public class MCH_BaseVehicleBoundingBox extends AxisAlignedBB {
    private final MCH_EntityBaseVehicle ac;
    private final MCH_VehicleBoxCache vehicleBoxCache = new MCH_VehicleBoxCache();

    protected MCH_BaseVehicleBoundingBox(MCH_EntityBaseVehicle ac) {
        super(ac.field_70121_D.field_72340_a, ac.field_70121_D.field_72338_b, ac.field_70121_D.field_72339_c, ac.field_70121_D.field_72336_d, ac.field_70121_D.field_72337_e, ac.field_70121_D.field_72334_f);
        this.ac = ac;
    }

    public AxisAlignedBB NewAABB(double minX, double minY, double minZ, double maxX, double maxY, double maxZ) {
        return new MCH_BaseVehicleBoundingBox(this.ac).func_72324_b(minX, minY, minZ, maxX, maxY, maxZ);
    }

    private MCH_BoundingBox[] getCalculatedExtraBoxes() {
        MCH_BoundingBox[] boxes = this.vehicleBoxCache.getCalculatedBoxes(this.ac);
        return boxes != null ? boxes : new MCH_BoundingBox[0];
    }

    public double getDistSq(AxisAlignedBB a, AxisAlignedBB b) {
        double ax = (a.field_72336_d + a.field_72340_a) / 2.0D;
        double ay = (a.field_72337_e + a.field_72338_b) / 2.0D;
        double az = (a.field_72334_f + a.field_72339_c) / 2.0D;
        double bx = (b.field_72336_d + b.field_72340_a) / 2.0D;
        double by = (b.field_72337_e + b.field_72338_b) / 2.0D;
        double bz = (b.field_72334_f + b.field_72339_c) / 2.0D;
        double dx = ax - bx;
        double dy = ay - by;
        double dz = az - bz;
        return dx * dx + dy * dy + dz * dz;
    }

    private boolean hasDeckCollision() {
        return this.ac instanceof MCH_EntityShip;
    }

    private boolean isDeckTopContact(AxisAlignedBB deck, AxisAlignedBB other, boolean zAxis) {
        boolean horizontalOverlap = zAxis
            ? other.field_72334_f > deck.field_72339_c && other.field_72339_c < deck.field_72334_f
            : other.field_72336_d > deck.field_72340_a && other.field_72340_a < deck.field_72336_d;
        return horizontalOverlap && other.field_72338_b >= deck.field_72337_e - 0.6D && other.field_72338_b <= deck.field_72337_e + 0.6D;
    }

    private boolean isDeckSupportContact(AxisAlignedBB deck, AxisAlignedBB other) {
        return other.field_72336_d > deck.field_72340_a && other.field_72340_a < deck.field_72336_d
            && other.field_72334_f > deck.field_72339_c && other.field_72339_c < deck.field_72334_f
            && other.field_72338_b >= deck.field_72337_e - 0.6D && other.field_72338_b <= deck.field_72337_e + 0.6D;
    }

    public double func_72316_a(AxisAlignedBB other, double offset) {
        if (!hasDeckCollision()) return offset;
        if (!isDeckTopContact(this, other, true)) offset = super.func_72316_a(other, offset);
        MCH_BoundingBox[] boxes = getCalculatedExtraBoxes();
        for (int i = 0; i < boxes.length; ++i) {
            if (!isDeckTopContact(boxes[i].boundingBox, other, true)) offset = boxes[i].boundingBox.func_72316_a(other, offset);
        }
        return offset;
    }

    public double func_72323_b(AxisAlignedBB other, double offset) {
        if (!hasDeckCollision()) return offset;
        offset = super.func_72323_b(other, offset);
        MCH_BoundingBox[] boxes = getCalculatedExtraBoxes();
        for (int i = 0; i < boxes.length; ++i) {
            AxisAlignedBB current = boxes[i].boundingBox;
            AxisAlignedBB previous = boxes[i].backupBoundingBox;
            offset = current.func_72323_b(other, offset);
            if (this.ac.canFloatWater() && current.field_72337_e > previous.field_72337_e && isDeckSupportContact(previous, other)) {
                offset = previous.func_72323_b(other, offset);
            }
        }
        return offset;
    }

    public double func_72322_c(AxisAlignedBB other, double offset) {
        if (!hasDeckCollision()) return offset;
        if (!isDeckTopContact(this, other, false)) offset = super.func_72322_c(other, offset);
        MCH_BoundingBox[] boxes = getCalculatedExtraBoxes();
        for (int i = 0; i < boxes.length; ++i) {
            if (!isDeckTopContact(boxes[i].boundingBox, other, false)) offset = boxes[i].boundingBox.func_72322_c(other, offset);
        }
        return offset;
    }

    public boolean func_72326_a(AxisAlignedBB other) {
        boolean hit = false;
        double nearest = 1.0E7D;
        this.ac.lastBBDamageFactor = 1.0F;
        this.ac.lastHitBoundingBoxType = EnumBoundingBoxType.DEFAULT;
        if (super.func_72326_a(other)) {
            nearest = getDistSq(other, this);
            hit = true;
        }
        MCH_BoundingBox[] boxes = getCalculatedExtraBoxes();
        for (int i = 0; i < boxes.length; ++i) {
            MCH_BoundingBox box = boxes[i];
            if (box.boundingBox.func_72326_a(other)) {
                double dist = getDistSq(other, this);
                if (dist < nearest) {
                    nearest = dist;
                    this.ac.lastBBDamageFactor = box.damegeFactor;
                    this.ac.lastHitBoundingBoxType = box.boundingBoxType;
                }
                hit = true;
            }
        }
        return hit;
    }

    public MovingObjectPosition func_72327_a(Vec3 start, Vec3 end) {
        this.ac.lastBBDamageFactor = 1.0F;
        this.ac.lastHitBoundingBoxType = EnumBoundingBoxType.DEFAULT;
        MovingObjectPosition result = super.func_72327_a(start, end);
        double nearest = result != null ? start.func_72438_d(result.field_72307_f) : 1.0E7D;
        MCH_BoundingBox[] boxes = getCalculatedExtraBoxes();
        for (int i = 0; i < boxes.length; ++i) {
            MCH_BoundingBox box = boxes[i];
            MovingObjectPosition candidate = box.boundingBox.func_72327_a(start, end);
            if (candidate != null) {
                double dist = start.func_72438_d(candidate.field_72307_f);
                if (dist < nearest) {
                    result = candidate;
                    nearest = dist;
                    this.ac.lastBBDamageFactor = box.damegeFactor;
                    this.ac.lastHitBoundingBoxType = box.boundingBoxType;
                }
            }
        }
        return result;
    }

    public AxisAlignedBB func_72314_b(double x, double y, double z) {
        return NewAABB(this.field_72340_a - x, this.field_72338_b - y, this.field_72339_c - z, this.field_72336_d + x, this.field_72337_e + y, this.field_72334_f + z);
    }

    public AxisAlignedBB func_111270_a(AxisAlignedBB other) {
        return NewAABB(Math.min(this.field_72340_a, other.field_72340_a), Math.min(this.field_72338_b, other.field_72338_b), Math.min(this.field_72339_c, other.field_72339_c), Math.max(this.field_72336_d, other.field_72336_d), Math.max(this.field_72337_e, other.field_72337_e), Math.max(this.field_72334_f, other.field_72334_f));
    }

    public AxisAlignedBB func_72321_a(double x, double y, double z) {
        double minX = this.field_72340_a;
        double minY = this.field_72338_b;
        double minZ = this.field_72339_c;
        double maxX = this.field_72336_d;
        double maxY = this.field_72337_e;
        double maxZ = this.field_72334_f;
        if (x < 0.0D) minX += x; if (x > 0.0D) maxX += x;
        if (y < 0.0D) minY += y; if (y > 0.0D) maxY += y;
        if (z < 0.0D) minZ += z; if (z > 0.0D) maxZ += z;
        return NewAABB(minX, minY, minZ, maxX, maxY, maxZ);
    }

    public AxisAlignedBB func_72331_e(double x, double y, double z) {
        return NewAABB(this.field_72340_a + x, this.field_72338_b + y, this.field_72339_c + z, this.field_72336_d - x, this.field_72337_e - y, this.field_72334_f - z);
    }

    public AxisAlignedBB func_72329_c() {
        return NewAABB(this.field_72340_a, this.field_72338_b, this.field_72339_c, this.field_72336_d, this.field_72337_e, this.field_72334_f);
    }

    public AxisAlignedBB func_72325_c(double x, double y, double z) {
        return NewAABB(this.field_72340_a + x, this.field_72338_b + y, this.field_72339_c + z, this.field_72336_d + x, this.field_72337_e + y, this.field_72334_f + z);
    }
}
