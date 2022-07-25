import os
import time

for jj in range(1,105):
    str0 = "python projector.py --outdir=out/projector" + str(jj) + " --target=out/ganstorage/final_imag00"+ str(jj) + ".jpg --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada/pretrained/ffhq.pkl"
    os.system(str0)
    time.sleep(15*60) 
