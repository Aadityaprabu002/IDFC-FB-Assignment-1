from functools import cmp_to_key
class Solution:
    #private
    __input = ''
    __output = ''
    __order_map = dict()
    def __read_input(self):
        with open('input.txt','r') as file:
            self.__input = file.read()

        
    def __write_output(self):
        with open('output.txt','w') as file:
            file.write(self.__output)
        pass
    
    def __classify_hand(self,card:str):
        label = dict()
        for c in card:
            if c in label:
                label[c]+=1
            else:
                label[c] = 1
        
        value = sorted(list(label.values()))
        if value == [5]:
            return 7
        elif value == [1,4]:
            return 6
        elif value == [2,3]:
            return 5
        elif value == [1,1,3]:
            return 4
        elif value == [1,2,2]:
            return 3
        elif value == [1,1,1,2]:
            return 2
        return 1

    def __compare(self,card1, card2):
        label1 = self.__classify_hand(card1)
        label2 = self.__classify_hand(card2)
        if label1 == label2:
            if card1 == card2:
                return 0
            
                
            for i in range(len(card1)):
                if  self.__order_map[card1[i]] >  self.__order_map[card2[i]]:
                    return 1
                elif  self.__order_map[card1[i]] <  self.__order_map[card2[i]]:
                    return -1
            return -1
        elif label1 > label2:
            return 1
        return -1
                
    def __logic(self):
        
        order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        for i,c in enumerate(reversed(order)):
            self.__order_map[c]=i


        cards = self.__input.split('\n')
        bids = []
        for card in cards:
            bids.append(int(card.split(' ')[1]))
        for i in range(len(cards)):
            card = cards[i].split(' ')
            cards[i] = card[0]
        
        cb_map = dict(zip(cards,bids))

        cards.sort(key=cmp_to_key(self.__compare))
        res = 0
        for i in range(len(cards)):
            card = cards[i]
            res += cb_map[card] * (i+1)
            
        self.__output = str(res)
        pass


    #public
    def run(self):
        self.__read_input()
        self.__logic()
        self.__write_output()

    def __init__(self):
        self.__input = ''
        self.__output = ''
        pass
    
if __name__ == '__main__':
    solution = Solution()
    solution.run()

