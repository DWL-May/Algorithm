/* 타로는 맛있는 키위 주스를 준비했습니다. 타로는 0부터 N-1이라 이름을 붙인 N개의 병에 키위주스를 넣었습니다.
이때 i 번째의 병의 용량은 capacities[i] 리터이며 타로가 i 번째 병에 넣은 키위 주스의 양을 bottles[i] 리터라고 합니다.

타로는 병에 키위 주스를 재분배하려고 하며, 0부터 M-1까지 M회 조작합니다. i번째의 조작은 타로가 병 fromId[i]부터
병 told[i]에 키위주스를 넣는 것을 의미합니다. 병 fromId[i]가 비어 있거나 병 told[i]가 꽉차 있는 순간,
타로는 더 이상 키위 주스를 넣지 않습니다.

N개의 요소를 가진 정수 배열 int[]를 리턴해주세요. 배열의 i 번째 요소는 모든 주스를 쏟는 작업이 완료되고
i번째 병에 남아 있는 키위주스의 양입니다.
 */

public class KiwiJuiceEasy {

    public static void main(String args[]){

        /*
        int[] capacities = {700000, 800000, 900000, 1000000};
        int[] bottles = {478478, 478478, 478478, 478478};
        int[] fromId = {2, 3, 2, 0, 1};
        int[] toId = {0, 1, 1, 3, 2};
        */

        int[] capacities = {14, 35, 86, 58, 25, 62};
        int[] bottles = {6, 34, 27, 38, 9, 60};
        int[] fromId = {1, 2, 4, 5, 3, 3, 1, 0};
        int[] toId = {0, 1, 2, 4, 2, 5, 3, 1};
        int[] result = thePouring(capacities, bottles, fromId, toId);

        for (int i = 0; i < result.length ; i++){

            System.out.println(result[i]);
        }
    }

    public static int[] thePouring(int[] capacities, int[] bottles, int[] fromId, int[] told){

        int fromCapacity;
        int toCapacity;
        int fromBottle;
        int toBottle;

        int[] result = new int[capacities.length];

        for (int i = 0; i < fromId.length; i++){
            fromCapacity = capacities[fromId[i]];
            toCapacity = capacities[told[i]];
            fromBottle = bottles[fromId[i]];
            toBottle = bottles[told[i]];

            if(toCapacity <= toBottle + fromBottle){
                fromBottle -= toCapacity - toBottle;
                toBottle = toCapacity;
            }else if (toCapacity > toBottle + fromBottle){
                toBottle = toBottle + fromBottle;
                fromBottle = 0;
            }

            bottles[told[i]] = toBottle;
            bottles[fromId[i]] = fromBottle;
        }
        return bottles;
    }
}
