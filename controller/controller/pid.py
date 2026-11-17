class PID():
    def __init__(self, k_p, k_i, k_d):
        self.k_p = k_p
        self.k_i = k_i;
        self.k_d = k_d
        self.integral = 0
        self.prev = None
        
    def output(self, sp, pv, dt):
        if(dt <= 0):
            raise ValueError("dt must be non-zero and positive!")
        
        e = sp - pv # error
        u_p = e * self.k_p # Proportional
        
        # Integral
        self.integral += e * dt 
        u_i = self.k_i * self.integral
        
        # Derivative
        if(self.prev is None): 
            u_d = 0 # only on the first call
        else: 
            u_d = ((e - self.prev) / dt ) * self.k_d
        
        self.prev = e
        return u_p + u_i + u_d 
    
    def reset(self):
        self.integral = 0
        self.prev = None