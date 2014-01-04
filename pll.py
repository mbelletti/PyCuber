from cube import *


def Aa_perm(c):
	"""
	L' B L' F2 L B' L' F2 L2
	"""
	return L2(F2(Li(Bi(L(F2(Li(B(Li(c)))))))))

def Ab_perm(c):
	"""
	R B' R F2 R' B R F2 R2
	"""
	return R2(F2(R(B(Ri(F2(R(Bi(R(c)))))))))

def E_perm(c):
	"""
	x R' U R D' R' U' R D R' U' R D' R' U R D
	"""
	return D(R(U(Ri(Di(R(Ui(Ri(D(R(Ui(Ri(Di(R(U(Ri(x(c)))))))))))))))))

def Ua_perm(c):
	"""
	R U' R U R U R U' R' U' R2
	"""
	return R2(Ui(Ri(Ui(R(U(R(U(R(Ui(R(c)))))))))))

def Ub_perm(c):
	"""
	R2 U R U R' U' R' U' R' U R'
	"""
	return Ri(U(Ri(Ui(Ri(Ui(Ri(U(R(U(R2(c)))))))))))

def H_perm(c):
	"""
	M2 U M2 U2 M2 U M2
	"""
	return M2(U(M2(U2(M2(U(M2(c)))))))

def Z_perm(c):
	"""
	M2 U M2 U M' U2 M2 U2 M' U2
	"""
	return U2(Mi(U2(M2(U2(Mi(U(M2(U(M2(c))))))))))

def Ja_perm(c):
	"""
	R' U L' U2 R U' R' U2 L R U'
	"""
	return Ui(R(L(U2(Ri(Ui(R(U2(Li(U(Ri(c)))))))))))

def Jb_perm(c):
	"""
	L U' R U2 L' U L U2 L' R' U
	"""
	return U(Ri(Li(U2(L(U(Li(U2(R(Ui(L(c)))))))))))

def T_perm(c):
	"""
	R U R' U' R' F R2 U' R' U' R U R' F'
	"""
	return Fi(Ri(U(R(Ui(Ri(Ui(R2(F(Ri(Ui(Ri(U(R(c))))))))))))))

def Ra_perm(c):
	"""
	L U2 L' U2 L F' L' U' L U L F L2 U
	"""
	return U(L2(F(L(U(L(Ui(Li(Fi(L(U2(Li(U2(L(c))))))))))))))

def Rb_perm(c):
	"""
	R' U2 R U2 R' F R U R' U' R' F' R2 U'
	"""
	return Ui(R2(Fi(Ri(Ui(Ri(U(R(F(Ri(U2(R(U2(Ri(c))))))))))))))

def F_perm(c):
	"""
	R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R
	"""
	return R(U(Ri(U(R(Ui(Ri(Ui(R2(F(Ri(Ui(Ri(U(R(Fi(Ui(Ri(c))))))))))))))))))

def V_perm(c):
	"""
	R' U R' d' R' F' R2 U' R' U R' F R F
	"""
	return F(R(F(Ri(U(Ri(Ui(R2(Fi(Ri(di(Ri(U(Ri(c))))))))))))))

def Na_perm(c):
	"""
	z D R' U R2 D' R D U' R' U R2 D' R U' R
	"""
	return R(Ui(R(Di(R2(U(Ri(Ui(D(R(Di(R2(U(Ri(D(z(c))))))))))))))))

def Nb_perm(c):
	"""
	z U' R D' R2 U R' D U' R D' R2 U R' D R'
	"""
	return Ri(D(Ri(U(R2(Di(R(Ui(D(Ri(U(R2(Di(R(Ui(z(c))))))))))))))))

def Y_perm(c):
	"""
	F R U' R' U' R U R' F' R U R' U' R' F R F'
	"""
	return Fi(R(F(Ri(Ui(Ri(U(R(Fi(Ri(U(R(Ui(Ri(Ui(R(F(c)))))))))))))))))

def Ga_perm(c):
	"""
	R2 u R' U R' U' R u' R2 y' R' U R
	"""
	return R(U(Ri(yi(R2(ui(R(Ui(Ri(U(Ri(u(R2(c)))))))))))))

def Gb_perm(c):
	"""
	R' U' R y R2 u R' U R U' R u' R2
	"""
	return R2(ui(R(Ui(R(U(Ri(u(R2(y(R(Ui(Ri(c)))))))))))))

def Gc_perm(c):
	"""
	R2 u' R U' R U R' u R2 y R U' R'
	"""
	return Ri(Ui(R(y(R2(u(Ri(U(R(Ui(R(ui(R2(c)))))))))))))

def Gd_perm(c):
	"""
	R U R' y' R2 u' R U' R' U R' u R2
	"""
	return R2(u(Ri(U(Ri(Ui(R(ui(R2(yi(Ri(U(R(c)))))))))))))

def None_perm(c):
	""
	return c

#cc = color_converter.color_convert

#Aa_test = cc("405000000111111111020222222333333333244444444552555555")
#Ab_test = cc("002000000111111111424222222333333333540444444255555555")
#E_test = cc("205000000111111111024222222333333333542444444450555555")
#Ua_test = cc("020000000111111111242222222333333333404444444555555555")
#Ub_test = cc("040000000111111111202222222333333333424444444555555555")
#H_test = cc("040000000111111111252222222333333333404444444525555555")
#Z_test = cc("050000000111111111242222222333333333424444444505555555")
#Jb_test = cc("500000000111111111222222222333333333455444444044555555")
#Ja_test = cc("550000000111111111222222222333333333445444444004555555")
#T_test = cc("040000000111111111224222222333333333502444444455555555")
#Ra_test = cc("520000000111111111202222222333333333445444444054555555")
#Rb_test = cc("500000000111111111242222222333333333425444444054555555")
#F_test = cc("000000000111111111254222222333333333542444444425555555")
#V_test = cc("400000000111111111225222222333333333054444444542555555")
#Na_test = cc("400000000111111111255222222333333333044444444522555555")
#Nb_test = cc("004000000111111111552222222333333333440444444225555555")
#Y_test = cc("450000000111111111225222222333333333044444444502555555")
#Ga_test = cc("545000000111111111022222222333333333450444444204555555")
#Gb_test = cc("252000000111111111405222222333333333044444444520555555")
#Gc_test = cc("242000000111111111405222222333333333024444444550555555")
#Gd_test = cc("525000000111111111052222222333333333440444444204555555")

#def test():
#	def goal(c):
#		for side in c:
#			color = side[1][1]
#			for cubie in side[0]+side[1]+side[2]:
#				if cubie != color:
#					return False
#		return True
#	for perm in "Aa Ab E Ua Ub H Z Ja Jb T Ra Rb F V Na Nb Y Ga Gb Gc Gd".split():
#		result = eval("%s_perm(%s_test)" % (perm, perm))
#		assert goal(result)
#	print "tests pass"