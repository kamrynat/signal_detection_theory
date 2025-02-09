import math

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
        
def criterion(self):
    