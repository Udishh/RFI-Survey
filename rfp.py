import math
from pylab import *
from rtlsdr import *

def plott(a):
	sdr = RtlSdr() 
	sdr.samplerate = 2.5e6 #the sample rate which decides the bandiwth of each band 
	sdr.centerfreq = float(a) #the central frequency 
	sdr.gain = 4 #the internal gain value to which each RTL would be set to

	samples = sdr.read_samples(1024*1024) # the number samples collected 
	sdr.close()
	power,freq=psd(samples, NFFT=1024, Fs=sdr.samplerate/1e6, Fc=sdr.centerfreq/1e6,return_line=False) #using the Matplotlib power spectral density function to obtain the power across each band and the corresponsding frequency
	power[512]=(1/2)*(power[510]+power[514]) # normalising the dc central spike in caused by the RTL
	power[511]=(1/2)*(power[510]+power[512])
	power[513]=(1/2)*(power[512]+ power[514])
	clf()
	xlabel('Frequency (MHz)')
	ylabel('Relative power (dB)')
	p=[]
	f=[]
	for i in range(len(freq)):
		if freq[i] > a/1e6 -.5 and freq[i] < a/1e6 +.5: #taking a central 1 Mhz of the 2.5 Mhz sampled to deal with voltage drops at the ends of the sampling width
        		f.append(freq[i])
        		p.append(10*math.log10(power[i]))			
	P=np.array(p)
	F=np.array(f)
	ylim(-54,0)
	yticks(np.arange(-54,0,10))
	plot(F,P)
	show()
	#savefig("plot" +str(a)+ ".jpg")


if __name__ == '__main__': 
    globals()[sys.argv[1]](sys.argv[2])
