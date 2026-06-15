package mcheli.aircraft;

import mcheli.MCH_Lib;
import net.minecraft.util.AxisAlignedBB;
import net.minecraft.util.Vec3;

public class MCH_BoundingBox {
    private static final double POS_EPSILON = 1.0E-5D;
    private static final float ROT_EPSILON = 1.0E-4F;
    public final AxisAlignedBB boundingBox;
    public final AxisAlignedBB backupBoundingBox;
    public final double offsetX;
    public final double offsetY;
    public final double offsetZ;
    public final float width;
    public final float height;
    public Vec3 rotatedOffset;
    public Vec3 nowPos;
    public Vec3 prevPos;
    public final float damegeFactor;
    public EnumBoundingBoxType boundingBoxType = EnumBoundingBoxType.DEFAULT;
    private boolean vehicleBoxCacheValid;
    private double cachedVehicleX;
    private double cachedVehicleY;
    private double cachedVehicleZ;
    private float cachedVehicleYaw;
    private float cachedVehiclePitch;
    private float cachedVehicleRoll;

    public MCH_BoundingBox(double x, double y, double z, float w, float h, float df) {
        offsetX=x; offsetY=y; offsetZ=z; width=w; height=h; damegeFactor=df;
        boundingBox = AxisAlignedBB.func_72330_a(x-w/2.0F, y-h/2.0F, z-w/2.0F, x+w/2.0F, y+h/2.0F, z+w/2.0F);
        backupBoundingBox = AxisAlignedBB.func_72330_a(x-w/2.0F, y-h/2.0F, z-w/2.0F, x+w/2.0F, y+h/2.0F, z+w/2.0F);
        nowPos = Vec3.func_72443_a(x, y, z);
        prevPos = Vec3.func_72443_a(x, y, z);
        updatePosition(0.0D, 0.0D, 0.0D, 0.0F, 0.0F, 0.0F);
    }
    public MCH_BoundingBox copy() { return new MCH_BoundingBox(offsetX, offsetY, offsetZ, width, height, damegeFactor); }
    public wheelBoundingBox copy2() { return new wheelBoundingBox(offsetX, offsetY, offsetZ, width, height, damegeFactor); }
    /** Cache identical transform requests as a behavior-preserving foundation for future oriented vehicle boxes. */
    public void updatePosition(double x, double y, double z, float yaw, float pitch, float roll) {
        if (vehicleBoxCacheValid && Math.abs(cachedVehicleX - x) <= POS_EPSILON && Math.abs(cachedVehicleY - y) <= POS_EPSILON && Math.abs(cachedVehicleZ - z) <= POS_EPSILON && Math.abs(cachedVehicleYaw - yaw) <= ROT_EPSILON && Math.abs(cachedVehiclePitch - pitch) <= ROT_EPSILON && Math.abs(cachedVehicleRoll - roll) <= ROT_EPSILON) return;
        cachedVehicleX = x; cachedVehicleY = y; cachedVehicleZ = z; cachedVehicleYaw = yaw; cachedVehiclePitch = pitch; cachedVehicleRoll = roll; vehicleBoxCacheValid = true;
        Vec3 v = Vec3.func_72443_a(offsetX, offsetY, offsetZ);
        rotatedOffset = MCH_Lib.RotVec3(v, -yaw, -pitch, -roll);
        float w = width; float h = height;
        double nx = x + rotatedOffset.field_72450_a;
        double ny = y + rotatedOffset.field_72448_b;
        double nz = z + rotatedOffset.field_72449_c;
        prevPos.field_72450_a = nowPos.field_72450_a; prevPos.field_72448_b = nowPos.field_72448_b; prevPos.field_72449_c = nowPos.field_72449_c;
        nowPos.field_72450_a = nx; nowPos.field_72448_b = ny; nowPos.field_72449_c = nz;
        backupBoundingBox.func_72328_c(boundingBox);
        boundingBox.func_72324_b(nx-w/2.0F, ny-h/2.0F, nz-w/2.0F, nx+w/2.0F, ny+h/2.0F, nz+w/2.0F);
    }
}
