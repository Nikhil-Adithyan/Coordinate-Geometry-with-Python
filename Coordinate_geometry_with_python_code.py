def find_triangle_coordinates(P, Q, R):
        
    p1, p2 = P[0], P[1]
    q1, q2 = Q[0], Q[1]
    r1, r2 = R[0], R[1]
        
    A = []
    B = []
    C = []
        
    a1 = p1 + r1 - q1
    a2 = p2 + r2 - q2
    b1 = q1 + p1 - r1
    b2 = q2 + p2 - r2
    c1 = r1 + q1 - p1
    c2 = r2 + q2 - p2
        
    A.append(a1)
    A.append(a2)
    B.append(b1)
    B.append(b2)
    C.append(c1)
    C.append(c2)
        
    return A, B, C
    
def find_triangle_area(A, B, C):
        
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]
    x3, y3 = C[0], C[1]
        
    area = (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)
    area = abs(area * 0.5)
        
    return area
    
def check_triangle_collinearity(A, B, C):
        
    area = find_triangle_area(A, B, C)
    if area == 0.0:
        message = str('Given vertices {}, {}, {} are collinear'.format(A, B, C))
    else:
        message = str('Given vertices {}, {}, {} are not collinear'.format(A, B, C))
    return message

def compare_triangles(triangle_area, midpoint_area):
    message = str('The area of triangle is {} times larger than the midpoint triangle'.format(int(triangle_area/midpoint_area)))
    return message

def plot_triangle(A, B, C, color):
    
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]
    x3, y3 = C[0], C[1]
    
    import matplotlib.pyplot as plt
    plt.rcParams['figure.figsize'] = (20, 10)
    plt.style.use('ggplot')
    
    fig = plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], color = color, linewidth = 2)
    plt.scatter([x1, x2, x3, x1], [y1, y2, y3, y1], color = 'red', linewidth = 3)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    return fig

def find_quadrilateral_area(A, B, C, D):
    
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]
    x3, y3 = C[0], C[1]
    x4, y4 = D[0], D[1]
    
    area = (x1*y2 + x2*y3 + x3*y4 + x4*y1) - (y1*x2 + y2*x3 + y3*x4 + y4*x1)
    area = abs(area * 0.5)
    return area

def check_quadrilateral_collinearity(A, B, C, D):
    
    area = find_quadrilateral_area(A, B, C, D)
    if area == 0.0:
        message = str('Given vertices {}, {}, {}, {} are collinear'.format(A, B, C, D))
    else:
        message = str('Given vertices {}, {}, {}, {} are not collinear'.format(A, B, C, D))
    return message

def plot_quadrilateral(A, B, C, D, color):
    
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]
    x3, y3 = C[0], C[1]
    x4, y4 = D[0], D[1]
    
    import matplotlib.pyplot as plt
    plt.rcParams['figure.figsize'] = (20, 10)
    plt.style.use('ggplot')
    
    fig = plt.plot([x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], color = color, linewidth = 2)
    plt.scatter([x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], color = 'b', linewidth = 3)
    plt.title('Quadrilateral for the given vertices A = {}, B = {}, C = {}, D = {}'.format(A, B, C, D), fontsize = 18)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    return fig

# Triangle

Pt, Qt, Rt = [12, 6], [11,4], [8,4]
At, Bt, Ct = find_triangle_coordinates([12, 6], [11,4], [8,4])
area_t = find_triangle_area(At, Bt, Ct)
area_mt = find_triangle_area(Pt, Qt, Rt)
ct = compare_triangles(area_t, area_mt)
collinearity_t = check_triangle_collinearity(At, Bt, Ct)

print('The given midpoints are P = {}, Q = {}, R = {}'.format(Pt, Qt, Rt))
print('The coordinates of triangle are A = {}, B = {}, R  {}'.format(At, Bt, Ct))
print('The area of the triangle is {} sq.units'.format(area_t))
print('The area of midpoint triangle is {} sq.units'.format(area_mt))
print(collinearity_t)
print(ct)

plot_triangle(At, Bt, Ct, 'black')
plot_triangle(Pt, Qt, Rt, 'b')

# Quadrilateral

Aq, Bq, Cq, Dq = [-4,-2], [-3,-5], [3,-2], [2,3]
area_q = find_quadrilateral_area(Aq, Bq, Cq, Dq)
collinearity_q = check_quadrilateral_collinearity(Aq, Bq, Cq, Dq)

print('The coordinates of quadrilateral are A = {}, B = {}, C = {}, D = {}'.format(Aq, Bq, Cq, Dq))
print('The area of quadrilateral is {} sq.units'.format(area_q))
print(collinearity_q)

plot_quadrilateral(Aq, Bq, Cq, Dq, 'r')