import math
class StatEngine:
    def init(self,data):
        if not data:
            raise TypeError("Empty data is invalid.")
        numbers=[]
        for num in data:
            if isinstance(num,(int,float)):
                numbers.append(num)
            else:
                raise TypeError("invalid data type")
        self.data=numbers

    #centeral tendency

    def get_mean(self):
        total=0
        for num in self.data:
            total +=num
        return total / len(self.data)
    def get_median(self):
        refined=sorted(self.data)
        n=len(self.data)
        mid=n//2
        if n%2==0:
            return (refined[mid-1] + refined[mid]) / 2
        else:
            return refined[mid]
    def get_mode(self):
        freq={}
        for num in self.data:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max_freq = max(freq.values())

        # All unique case
        if max_freq == 1:
            return "No mode (all values are unique)"

        modes = []

        # Multimodal support
        for num in freq:
            if freq[num] == max_freq:
                modes.append(num)

        return modes


    #variance and standard deviation
    def get_variance(self,sample=True):
        mean = self.get_mean()
        n=len(self.data)
        if n==0:
            raise TypeError("data cannot be empty")
        total=0
        for num in self.data:
            total +=(num-mean) ** 2
        if sample:
            if n < 2:
                raise TypeError("it must be atleast 2 values")
            return total /(n-1)
        else:
            return total /n
    def get_standard_deviation(self,sample=True):
        return math.sqrt(self.get_variance(sample))
    
    # outliers

    def get_outliers(self,threshold=2):
        mean=self.get_mean()
        std=self.get_standard_deviation()

        if std ==0:
            return []

        return [
            x for x in self.data
            if abs(x-mean) / std > threshold
        ]
if name =="main":

    user=input("enter number :")
    try:
        data = [float(x) for x in user.split()]
        engine = StatEngine(data)

        print("Mean :" ,engine.get_mean())
        print("Median :" ,engine.get_median())
        print("Mode :" ,engine.get_mode())
        print("sample variance :" ,engine.get_variance(True))
        print("population variance :" ,engine.get_variance(False))
        print("standard deviation :" ,engine.get_standard_deviation())
        print("outliers :" ,engine.get_outliers())
    except ValueError:
        print("error: enter valid numbers")
    except TypeError as e:
        print("error:" , e)
