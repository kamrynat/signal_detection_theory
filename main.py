import math
import scipy

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections
        
    def hit_rate(self):
        H = self.hits / (self.hits + self.misses)
        return H

    def false_alarm_rate(self):
        FA = self.false_alarms / (self.false_alarms + self.correct_rejections) 
        return FA
    
    def d_prime(self):
        '''hit_rate = self.hit_rate()
        fa_rate = self.false_alarm_rate()
        
        # Handle edge cases
        hit_rate = np.clip(hit_rate, 0.00001, 0.99999)
        fa_rate = np.clip(fa_rate, 0.00001, 0.99999)
        
        z_hit = norm.ppf(hit_rate)
        z_fa = norm.ppf(fa_rate)
        
        return z_hit - z_fa'''
    
    def criterion(self):
        '''hit_rate = self.hit_rate()
        fa_rate = self.false_alarm_rate()
        
        # Handle edge cases
        hit_rate = np.clip(hit_rate, 0.00001, 0.99999)
        fa_rate = np.clip(fa_rate, 0.00001, 0.99999)
        
        z_hit = norm.ppf(hit_rate)
        z_fa = norm.ppf(fa_rate)
        
        return -0.5 * (z_hit + z_fa)'''