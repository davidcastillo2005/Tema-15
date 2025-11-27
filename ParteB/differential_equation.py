def dz_dt(M, z):
    return M * z - z ** 3
    # return z * (M + z) * (M - z)