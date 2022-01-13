import matplotlib.pyplot as plt
import numpy as np

f_name = 'superresolution/swinir_sr_classical_patch48_x3_crop_5/train.log'
f_log = open(f_name, 'r')
lines = f_log.readlines()

psnrs = [0.0]
losses = [0.15]
iters_psnr = [0]
iters_loss = [0]
for line in lines:
    if 'Average PSNR' in line:
        itr = int(line.split('iter: ')[1].split(
            ', Average PSNR')[0].replace(',', ''))
        psnr = float(line.split(', Average PSNR : ')[1][:-3])
        psnrs.append(psnr)
        iters_psnr.append(itr)
    if 'G_loss: ' in line:
        itr = int(line.split('iter: ')[1].split(', lr:')[0].replace(',', ''))
        loss = float(line.split('G_loss: ')[1])
        iters_loss.append(itr)
        losses.append(loss)


plt.plot(iters_psnr, psnrs)
plt.xlabel('iteration')
plt.ylabel('psnr')
plt.xticks(np.arange(min(iters_psnr), max(iters_psnr), 100000))
plt.yticks(np.arange(0, 32, 2))
plt.grid()
plt.title('Training History (psnr)')
plt.savefig('psnr.png')
plt.show()

plt.plot(iters_loss, losses)
plt.xlabel('iteration')
plt.ylabel('G_loss')
plt.xticks(np.arange(min(iters_loss), max(iters_loss), 100000))
plt.yticks(np.arange(0, 0.2, 0.01))
plt.grid()
plt.title('Training History (G_loss)')
plt.savefig('loss.png')
plt.show()
