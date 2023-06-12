from w_no_apapt import *
import math

def W_2(vals, index, predicted_val):
   entropy_little, entropy_big, distr_little, distr_big,  num_little,  num_big = prepare(vals, index, predicted_val)

   coined_entropy_big = 0
   for p in distr_big:
      coined_entr = entropy_coin(p)
      coined_entropy_big += coined_entr

   big_w = coined_entropy_big


   coined_entropy_lit = 0
   for p in distr_little:
      coined_entr = entropy_coin(p)
      coined_entropy_lit += coined_entr

   lit_w = coined_entropy_lit

   print ("     lit_w = " + '%.2f' % lit_w + " big_w = " + '%.2f' % big_w)


def W_1(vals, index, predicted_val):
   entropy_little, entropy_big, distr_little, distr_big,  num_little,  num_big = prepare(vals, index, predicted_val)
   FULL_MASS = MAX_ENTR_OF_COIN*(len(distr_big) + len(distr_little))

   coined_entropy_lit = 0
   for p in distr_little:
      coined_entr = entropy_coin(p)
      coined_entropy_lit += coined_entr



   ECLUDED_MASS = coined_entropy_lit
   w = FULL_MASS - ECLUDED_MASS
   print ("            w = " + '%.2f' % w )

if __name__ == '__main__':
   w_func = W_1
   test_1(w_func)
   test_2(w_func)
   test_3(w_func)
   test_4(w_func)