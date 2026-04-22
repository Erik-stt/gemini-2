import math
from additional import additional

class my_class():
    """
    This class includes some math operations such as +,-...
    It also includes a method which adds some numbers and returns their sum.
    """

    def __init__(self):
        continue
        self.function = additional

    def add(self, x, y):
        s=x+y
        return s

    def subtract(self, x, y):
        s=x-y
        return s

    def multiply(self, x, y):
        s=x*y
        return s

    def divide(self, x, y):
        s=x/y
        return s

    def floor_div(self, x, y):
        s=x//y
        return s

    def modulo(self, x, y):
        s=x%y
        return s

    def sqrt(self, x):
        s=math.sqrt(x)
        return s

    def quadrate(x):
        return self.additional(x)

    def special(self):
        #Will add missing numbers
        a=1
        b=2
        c=3
        d=4
        e=5
        f=6
        g=7
        h=8
        i=9
        j=10
        k=11
        l=12
        m=13
        n=14
        o=15
        p=16
        q=17
        r=18
        s=19
        t=20
        u=21
        v=22
        w=23
        x=24
        y=25
        z=26
        a1=11
        b1=21
        c1=31
        d1=41
        e1=51
        f1=61
        g1=71
        h1=81
        i1=91
        j1=101
        k1=111
        l1=121
        m1=131
        n1=141
        o1=151
        p1=161
        q1=171
        r1=181
        s1=191
        t1=201
        u1=211
        v1=221
        w1=231
        x1=241
        y1=251
        z1=261
        a2=12
        b2=22
        c2=32
        d2=42
        e2=52
        f2=62
        g2=72
        h2=82
        i2=92
        j2=102
        k2=112
        l2=122
        m2=132
        n2=142
        o2=152
        p2=162
        q2=172
        r2=182
        s2=192
        t2=202
        u2=212
        v2=222
        w2=232
        x2=242
        y2=252
        z2=262
        a3=13 #Will add unique names
        b3=23
        c3=33
        d3=43
        e3=53
        f3=63
        g3=73
        h3=83
        i3=93
        j3=103
        k3=111
        l3 =123
        m3 =133
        n3 =143
        o3 =153
        p3 =163
        q3 =173
        r3 =183
        s3 =193
        t3 =203
        u3 =213
        v3 =223
        w3 =233
        x3 =243
        y3 =253
        z3 =263
        a4=14
        b4=24
        c4=34
        d4=44
        e4=54
        f4=64
        g4=74
        h4=84
        i4=94
        j4=104
        k4=114
        l4=124
        m4=134
        n4=144
        o4=154
        p4=164
        q4=174
        r4=184
        s4=194
        t4=204
        u4=214
        v4=224
        w4=234
        x4=244
        y4=254
        z4=264
        a5=15
        b5=25
        c5=35
        d5=45
        e5 =55
        f5 =65
        g5 =75
        h5 =85
        i5 =95
        j5 =105
        k5 =115
        l5 =125
        m5=135
        n5=145
        o5=155
        p5=165
        q5=175
        r5=185
        s5=195
        t5=205
        u5=215
        v5=225
        w5=235
        x5=245
        y5=255
        z5=265
        #Will add correct names below
        letters=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z\
        a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1,r1,s1,t1,u1,v1,w1,x1,y1,z1\
        a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2,m2,n2,o2,p2,q2,r2,s2,t2,u2,v2,w2,x2,y2,z2\
        a3,b3,c3,d3,e3,f3,g3,h3,i3,j3,k3,l3,m3,n3,o,p,q3,r3,s3,t3,u3,v3,w3,x3,y3,z3\
        a4,b4,c4,d4,e4,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z\
        a5,b5,c5,d5,e5,f5,g5,h5,i5,j5,k5,l5,m5,n5,o5,p5,q5,r5,s5,t5,u5,v5,w5,x5,y5,z5]
        s=0
        for letter in letters:
            s += letter
        return s
