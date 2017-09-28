import psonic as p
import random

def tests():
	for i in range(5):
		p.play(random.randrange(60,80))
		p.sleep(1)

#tests()
#p.play(':d4')
for i in range(10):
	p.sample('drum_heavy_kick')
	p.sleep(0.5)
	p.sample('drum_snare_hard')
	p.sleep(0.5)
	p.sample('drum_heavy_kick')
	p.sleep(0.5)
	p.play(random.randrange(60,80))
	p.sleep(0.5)
