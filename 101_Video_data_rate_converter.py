################################
# Video Rate Conversion
################################

def data_megabits(bit_depth, hor_res, vert_res, frames_per_sec):
    byte_depth = bit_depth/8
    size = byte_depth * hor_res * vert_res * frames_per_sec
    size_in_GB = size/(1024**3)
    return print(f"Size in GB of one hour of uncompressed video with {bit_depth} bit depth, {hor_res} * {vert_res } resolution and {frames_per_sec} frames per second = " + str(size_in_GB*3600) + " GB")

print(data_megabits(8,640,240,24))
print(data_megabits(10,640,480,30))
print(data_megabits(24,1280,720,30))
print(data_megabits(24,1280,720,60))
print(data_megabits(24,1920,540,60))

def data_gigabits(bit_depth, hor_res, vert_res, frames_per_sec):
    byte_depth = bit_depth / 8
    size = byte_depth * hor_res * vert_res * frames_per_sec
    size_in_TB = (size/1024**4)
    return print(f"Size in TB of one hour of uncompressed video with {bit_depth} bit depth, {hor_res} * {vert_res } resolution and {frames_per_sec} frames per second = " + str(size_in_TB*3600) + " TB")

# some examples
print(data_gigabits(24,1920,1080,60))
print(data_gigabits(24,3840,2160,60))
print(data_gigabits(24,3840,2160,120))
print(data_gigabits(24,8192,4320,30))



