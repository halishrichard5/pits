from scipy.fft import fft, ifft
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
y
array([ 4.5 +0.j , 2.08155948-1.65109876j,
 -1.83155948+1.60822041j, -1.83155948-1.60822041j,
 2.08155948+1.65109876j])
yinv = ifft(y)
