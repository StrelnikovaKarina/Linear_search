import time


counter = 3        # количество сравнений
sleep = 1           # время прирывания программы
clock_counter = 0      # количество раз когда time.clock() была точнее
time_counter = 0       # количество раз когда time.time() была точнее

# в цикле расчитывается время выполнения time.sleep(sleep) с помощью time.clock() и time.time()
# и считается какая функция делала это более точно
# увеличивая значение sleep и counter можно добиться большей точности

while counter != 0:
    start_clock = time.clock()
    time.sleep(sleep)
    elapsed_clock = (time.clock() - start_clock)

    start_time = time.time()
    time.sleep(sleep)
    elapsed_time = (time.time() - start_time)

    difference_c = abs(sleep - elapsed_clock)
    difference_t = abs(sleep - elapsed_time)

    if difference_c < difference_t:
        clock_counter += 1
    elif difference_c == difference_t:
        clock_counter += 1
        time_counter += 1
    else:
        time_counter += 1
    counter -= 1

print('time.sleep() : ', sleep, 'second(s)')
print('time.clock() : ', elapsed_clock, 'second(s)')
print('time.time() : ', elapsed_time, 'second(s)')
print('=======')

if clock_counter < time_counter:
    print("time.time() is more correct")
elif time_counter < clock_counter:
    print("time.clock() is more correct")
else:
    print("time.time() and time.clock() are the same")