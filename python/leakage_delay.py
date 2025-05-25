import numpy as np
import matplotlib.pyplot as plt

# grc_parameter
filename = "/home/orkun-alp/Documents/fmcw_bitirme_calismalari/radar_parameter/dead_time_calc/chirp_leae_analysis_fiinish.dat"  # tam yol burası
fs = 6e6               # sample rate
chirp_time = 1 / 1e6  # chirp periyodu = 40 µs
chirp_bw = 1e6         # chirp bandwidth = 1 MHz
mu = chirp_bw / chirp_time  # sweep rate (Hz/s)
fft_size = 8192       # fft çözünürlüğü

# read_file
data = np.fromfile(filename, dtype=np.complex64)

# fft_calc and db_converter
spectrum = np.fft.fftshift(np.fft.fft(data[:fft_size]))
magnitude = 20 * np.log10(np.abs(spectrum))

# frequnecy_domain
freqs = np.fft.fftshift(np.fft.fftfreq(fft_size, d=1/fs))

# peak_frequency
peak_bin = np.argmax(magnitude)
f_beat = freqs[peak_bin]

# latency_calc
tau = f_beat / mu        # saniye cinsinden
tau_ns = tau * 1e9       # nanosaniye cinsinden

# write_results
print(f"Peak bin: {peak_bin}")
print(f"f_beat: {f_beat:.2f} Hz")
print(f"τ (delay): {tau_ns:.2f} ns")

# plot
plt.figure(figsize=(10, 4))
plt.plot(freqs / 1e3, magnitude)
plt.title("FFT Magnitude Spectrum")
plt.xlabel("Frequency (kHz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.tight_layout()
plt.show()
