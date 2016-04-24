import matplotlib

# définition de la fonction

def f(t):
    s1 = cos(2*pi*t)
    e1 = exp(-t)
    return multiply(s1, e1)

# tableau de données

x = [-1, 0, 1, 2]
y = [3, 2, 4, 1]

plot(x, y)
show()

# orthonormal

axis('equal')

# grille

grid()


t1 = arange(0.0, 5.0, 0.1)
t2 = arange(0.0, 5.0, 0.02)
t3 = arange(0.0, 2.0, 0.01)

subplot(211)
l = plot(t1, f(t1), 'bo', t2, f(t2), 'k--', markerfacecolor='green')
grid(True)
title('2 graphiques ensemble')
ylabel('des oscillations')

subplot(212)
plot(t3, cos(2*pi*t3), 'r.')
grid(True)
xlabel('temps (s)')
ylabel('encore des oscillations')
show()
