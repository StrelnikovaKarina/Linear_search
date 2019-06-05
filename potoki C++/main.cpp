#include <iostream>
#include <thread>
#include <chrono>

void Do(){
    // цикл для вывода ID потока с задержкой (для Do)
    for (size_t i=0; i<10; i++){
        std::cout <<"ID potoka - "<< std::this_thread::get_id()<<"\tDo\t" << i << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(700));
    }
}
int main() {
    std::thread th(Do);

    // цикл для вывода ID потока с задержкой (для main)
    for (size_t i=0; i<10; i++){
        std::cout <<"ID potoka - "<< std::this_thread::get_id()<<"\tmain\t" << i << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(300));
    }
    th.join(); //дождется выполнения всех потоков, а не только главного
    return 0;
}