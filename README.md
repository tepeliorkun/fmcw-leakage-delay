# fmcw-leakage-delay
FMCW radar leakage delay estimation and USB data rate analysis using ADALM-PLUTO SDR.
    In the system designed with GNU Radio, a Timer block was used to collect data for a specific duration. The signals received from the SDR device were saved in .dat format, with each file corresponding to a fixed capture period.

Using Python, the number of samples in each .dat file was analyzed to calculate the actual duration of the recorded data. This approach enabled a comparative analysis of the RNDIS and ECM USB protocols in terms of:

    Data transfer efficiency

    Sustained capture duration without loss

    Practical sustainable bandwidth performance
        In the second part of the project, an FMCW chirp signal was transmitted from the system, and the leakage signal received at the RX side was recorded in .dat format. This data was then analyzed using Python.

The analysis script performs a Fast Fourier Transform (FFT) on the recorded signal to identify the dominant frequency component (f_beat). This beat frequency is then divided by the chirp’s sweep rate (μ) to calculate the hardware delay between the TX and RX paths, expressed in nanoseconds.

    This method provides a direct and effective way to observe internal hardware latency in SDR devices such as the ADALM-PLUTO.
