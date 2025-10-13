class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0

        secret_count = {}
        guess_count = {}

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] = secret_count.get(s, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1
        
        for ch in guess_count:
            if ch in secret_count:
                cows += min(guess_count[ch], secret_count[ch])
        return str(bulls) + 'A' + str(cows) + 'B'