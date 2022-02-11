
def main(string_val, hash_dict):
    
    def print_increment(first_word, total_list, hash_dict):
        if first_word and total_list not in hash_dict:
            hash_dict.add(total_list)
            print(first_word, total_list, total_list+(first_word))
            total_list=total_list+(first_word)
            
        if not total_list:
            return
        #return print_increment(total_list[0],total_list[1:], hash_dict)
        for ix in range(0,len(total_list)):
            print_increment(total_list[ix], total_list[ix+1:], hash_dict)
    print_increment(string_val[0],string_val[1:], hash_dict)

hash_dict=set()
main("abhishek", hash_dict)