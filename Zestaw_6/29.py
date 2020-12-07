tab = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
n = len(tab)

def trididist(x,y,z):
    return ((x**2) + (y**2) + (z**2))**(1/2)


def recur_mass_center_epic_black_hole_very_cool_zadanie_10outof10(T, N, x=0, y=0, z=0, num_points=0, i=0):
    if i == N:
        if num_points >= 3:
            return x/num_points, y/num_points, z/num_points
        return 9999, 9999, 9999
    n_x, n_y, n_z = T[i][0], T[i][1], T[i][2]
    r1 = recur_mass_center_epic_black_hole_very_cool_zadanie_10outof10(T, N, x+n_x, y+n_y, z+n_z, num_points+1, i+1)
    r2 = recur_mass_center_epic_black_hole_very_cool_zadanie_10outof10(T, N, x, y, z, num_points, i+1)
    return min(r1, r2)

print(recur_mass_center_epic_black_hole_very_cool_zadanie_10outof10(tab,n))