"""
https://leetcode.com/problems/permutation-in-string/
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
#incomplete
"""
class Solution(object):
    def brute_force(self,s1,s2):
        sorted_s1="".join(sorted(s1))
        for ele in range(0,len(s2)):
            print(s2[ele:ele+2])
            if sorted_s1=="".join(sorted(s2[ele:ele+2])):
                return True
        return False

    def _permute(self, s1):
        state=[]
        result=set()
        s1=list(s1)
        self.find_permutation(s1,state,result)
        return result


    def find_permutation(self,s1_list, state,result):
        if not s1_list:
            result.add( "".join(state))
            return
        for idx in range(len(s1_list)):
            state.append(s1_list[idx])
            self.find_permutation(s1_list[:idx]+s1_list[idx+1:],state,result)
            state.pop()
    
    def _swap(self,s,idx,i):
        s=list(s)
        s[idx],s[i]=s[i],s[idx]
        return "".join(s)

    def _permuatation_helper(self,idx, s,result):
        if idx==len(s)-1:
            result.add("".join(s))
            return
        for i in range(idx,len(s)):
            s=self._swap(s,idx,i)
            self._permuatation_helper(idx+1,s,result)
            s=self._swap(s,idx,i)


    def permute(self,s):
        i=0
        result=set()
        self._permuatation_helper(i,s,result)
        return result


    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #return self.brute_force(s1,s2)
        permutation_strings = self.permute(s1)
        print(permutation_strings)
        for ele in permutation_strings:
            if ele in s2:
                return True
        return False


s1="ab";s2="eidbaooo"
s1="abc"
#s1="trfhcbogglim"

#s2="amwfpqwfwkarvhfcisywzaahtbdbuicxmjseeoudwfcdxetbmacayfikolbdxkocezhalfhxabwvuddcyazwiqiwefgolzvrpdxcuskpsmwhslpeygjrvvajajafppcwkqhxwkigemfullbqkvuqwfnqnhxiltyfcpfdyumfwyelmtzbdccmbvxedgfimmsqwxmopvxmuonuzyzlhpeunailpydcqybghdwvqxrpautsvrhfxprdqlgzownvincoxjnjwrqrdgpegtgvlifbbautkfqbhqiftbmxadvorqjnqlsceuctazxgofmchypspqvwyzoeejqfkvvwftvagajafmafvytslubpzalnahjknarjswkxmzzlmlokrifiopjcamvynmmuegnzvveetssuucqclbzxgjwbsflyelpdsvzicdnlenuxggcsrckfdixsqcjrzsbztgvxbpktlbdqrcqoatgxqhwehqiuqjnldursyzplwlcdvwrmlknviqtexwgqovwbcdugdblakufxcapvkvhraacetowtcypfxlvwmwdafesfgqezspbvqzxicblrdsmmdzunpcmzvysgbnspuldkppwlrsrnnewwjquhzrodmsbgbycvrzmtnskyuqqoqkxyakojewbbtntbdjuncpgbwgrtvewyscyujnqtpuaulrnjqmdujxydwzfyqfnxmjqogibxqeuqdxsdjjpootpzmhcvoeyvdspktyjzadkfwcdulsuktottgpvptjfydvpdxoznzhbkmitaiywqklwrktmzsyndnqmtapaaadzkynfxiwqxtekcbkmcwhwwdylvoxosxcexeceavpfptdlkyinhdobrnxfdbtuomjojmzeytlntkundrydqmkiayounnbhfxrlriuatzumgfcyniicwhtsaffhnxamwjtgbxvewtgovvrjvblrlvrghyoiicgvyorzjgecmxqeiwpuubfrnkmpynwywqczqdpeinebgfyrhouvifthoaariadurpbrexbfnuwgkbmgowjuaysnmidptzetckscxvxttdogpywxdvaktmkispgyghfazxyxslyjhqorndzpjepmwiuisfhvacnpkthbfrasndrfkfuhpetlnfugmqhqpvtvlwumhxduxxmugstcbksvqholothhftzungtxdysudnixkzekpdlgddnvyfuitcedxvjfsjxhbcrenufafxzdrumeavumdbvvgpodgtsjzznxkpbfltchmogigordwcpcanomjznfmsxpzqgxigjpybooxsgyiuxskowkdpypnzpgebowqefomcpmfilixgzvoffvmcypgyrwhwaelfpclzaoldlaimtnszckziyqewrtewpfyhphxruytifwtodznvxmxwoibqvtmynpqshnmiymrayaenoiknjqzwoltqhaganjdwzkncathqrgcigaguimqgznupmsikurxjltfydqiozmddxydgtsvwoloqtlqhryfqmcsfetvtjkauyjgillobotqfhzsyjtcjsiqxhwoaucluagbltdwroayydlwzytpqlsxkbrgcavvaqvlggewskeflsejklqexjvcudzaanxrgnkwygokcuxkvypsh"
print(Solution().checkInclusion(s1,s2))