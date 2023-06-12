
import math



def entropy_coin(p):
   p1 = p
   p2 = 1 - p
   if p1 == 0 or p2 == 0:
      return 0
   entropy = -p1* math.log(p1) - p2* math.log(p2)
   return entropy

MAX_ENTR_OF_COIN = entropy_coin(0.5)

def prepare(vals, index, predicted_val):
   print ("-------------------------------------------")
   # получаем массив ошибок как ненормированную пока величину
   # берем два подмассива - ошибка больше ошибки на целевом символе и меньше
   # нормируем, чтоб получилось распределение вер-тей на объединенном массиве
   # считаем вклад в энтропию от массива с меньшими ошибками
   # чем больше этот вклад, тем хуже, поэтому возвращаем чтото другое

   abs_err_on_target = abs(predicted_val - vals[index])
   abs_errors_big = []
   abs_errors_little = []

   for val in vals:
      val_err = abs(predicted_val - val)
      if  val_err > abs_err_on_target:
         abs_errors_big.append(val_err)
      else:
         abs_errors_little.append(val_err)

   divider = sum(abs_errors_little) + sum(abs_errors_big)

   distr_big = list([x/divider for x in abs_errors_big])
   distr_little = list([x / divider for x in abs_errors_little])


   entropy_big = None
   if len(distr_big)>0:
      entropy_big = 0
      for p in distr_big:
         if p != 0:
            entropy_big -= p*math.log(p)

   entropy_little = None
   if len(distr_little) > 0:
      entropy_little=0
      for p in distr_little:
         if p!=0:
            entropy_little -= p * math.log(p)
   num_little = len(distr_little)
   num_big = len(distr_big)
   return entropy_little, entropy_big, distr_little, distr_big,  num_little,  num_big







def test_1(w_func):
   print("")
   print('\033[95m' + "===================================================")
   print("                Должно уменьшаться:    " + '\033[0m')
   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.7
   w_func(vals_, index_, predicted_val_)

   vals_ = [1, 1, 1, 3]
   index_ = 0
   predicted_val_ = 0.7
   w_func(vals_, index_, predicted_val_)


def test_2(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Должно уменьшаться:    " + '\033[0m')
   vals_ = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.8
   w_func(vals_, index_, predicted_val_)

   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.8
   w_func(vals_, index_, predicted_val_)



def test_3(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Примерно одинаково    " + '\033[0m')
   vals_ = [1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w_func(vals_, index_, predicted_val_)

   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.8
   w_func(vals_, index_, predicted_val_)


def test_4(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Должно увеличиваться    " + '\033[0m')
   vals_ = [1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w_func(vals_, index_, predicted_val_)

   vals_ = [1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 1
   w_func(vals_, index_, predicted_val_)


def test_5(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Должно увеличиваться    " + '\033[0m')
   vals_ = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w_func(vals_, index_, predicted_val_)

   vals_ = [1, 1, 1, 1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 1
   w_func(vals_, index_, predicted_val_)
