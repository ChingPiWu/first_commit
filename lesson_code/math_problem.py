def fibonacci_sequence(max_limit = 10000):
  a, b = 0, 1
  fibonacci_sequence = []
  while a < max_limit:
    fibonacci_sequence.append(a)
    a, b = b, a + b
  return fibonacci_sequence

def prime(max_limit = 10000):
    n=2
    s=[]
    while n < max_limit:
        for i in s:
            if n%i==0:
                break
        else:
            s.append(n)
        n+=1
    return s
def right_angle(edge_1,edge_2):
  answer=list()
  answer+=[(edge_1 ** 2 + edge_2 ** 2)**0.5]
  if edge_1 != edge_2:
    answer+=[abs(edge_1 ** 2 - edge_2 ** 2)**0.5]
  return answer

if __name__ == '__main__':
  n = 100
  print(f'Fibonacci Numbers List:<{n}',fibonacci_sequence(n))
  print(f'Prime Numbers List:<{n}',prime(n))
  
  edge_1 = 3
  edge_2 = 4
  print(f'Given 2 known edge: {edge_1,edge_2}, return two possible answer:', right_angle(edge_1,edge_2))
else:
  print('DEF: ', __name__)
