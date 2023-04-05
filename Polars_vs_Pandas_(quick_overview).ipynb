{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "![Polars_vs_pandas_img.jpg](data:image/jpeg;base64,/9j/4QCARXhpZgAATU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAABIAAAAAQAAAEgAAAABAAKgAgAEAAAAAQAAAzSgAwAEAAAAAQAAATgAAAAA/9sAQwAGBgYGBwYHCAgHCgsKCwoPDgwMDg8WEBEQERAWIhUZFRUZFSIeJB4cHiQeNiomJio2PjQyND5MRERMX1pffHyn/9sAQwEGBgYGBwYHCAgHCgsKCwoPDgwMDg8WEBEQERAWIhUZFRUZFSIeJB4cHiQeNiomJio2PjQyND5MRERMX1pffHyn/8AAEQgBOAM0AwEiAAIRAQMRAf/EAB0AAQACAgMBAQAAAAAAAAAAAAAHCAUGAwQJAQL/xABWEAABAwMBBQQFBwYKBggHAQABAAIDBAURBgcSITFBE1FhcQgUIoGhIzJCUpGxwRUWM2JyghckQ1NzkpOywtEYJTRjo+FWZJSis7TT8Sg1RGV0ddLw/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/ALUoiICIiAiIgIiICIiAiIgIiICIiAiIgIiiTaPtXtWjo3UkDWVd1ezLKcH2IgeTpSOQ7m8yglKqq6WjgfUVVRFBCwZfJI8MY0eJdgBRVd9uGz22vcxlwlrXtOCKWIvHuc7dafcVTHUusNRanqzUXavkmwSWRZ3Yo/BjBwHnzPVauguS/wBJHTAf7FluRb3nswfs3is3bfSA0DVva2oNdRnq6aHeb9sRefgqNog9PLPf7Je6ft7Xcqerj6mJ4cW56OHMHwKzC8u7dc7ja6uOroKyamnZ82SJ5Y4eGR0PUK1uzfbpHcJYLXqZ0cVQ4hsVcAGRvPQSjk0n6w4eSCy6IiAiIgIiICLrS1lJEcSVMTD+s8D71wtudtccCupyfCRv+aDvouKOeGX9HKx/7LgfuXKgIiICIiAi43vaxrnvcGtaCS4nAAHMkqrW0Xby9ks9t0q9uGktkuBAdk8j2IPDH6x9yCxl71LYLDD2t1ulNStIy0SPAc79lvN3uCiq4ekFoKlc5tOLhV45OihDWn+1cw/BUpra6sr6mSprKmWeeQ5fLK4ve4+JOcrpoLmx+kfpIuxJabo1veGxOP2b4W52bbNs+uz2Rtu/qsjjgMqmGEf1zlo+1ef6IPU+KaKaNssUjXscMte0hwI7wRzC5V5w6S1/qfSdQ19trndhnL6WQl8D+/Leh8Rgq62z/aVZdaUh7H+L18TQZ6R5yQPrMP0mePTqgkhERAREQEREBF85cSq3662y1ktx/N7RcJq617+ydVMb2gDurYW8Q4jq48AgnO+amsGn4BNdrpT0rSCWiR/tOx9Vo9p3uCiK5+kPoqle5lJTXCsI5PbG2Nh97yHfBa3p7YPWXOb8p6zu1RNUy+0+njk3357pJXZz5N+1TXatnmiLSxraTTtCC3k+SMTP/rybzvighpvpK2kv9rTtUG94mYT9mAtstO3zQVe9rKh9ZQuPDM8W83PnEX8PE4UtOstnczcdbaQt+qYWEfctPvOyrQN4Y4T2CmheRwlpm+ruB7/k8AnzBQbnbrpbbpTNqaCtgqYHcpIXh7c92W54+CyCqdeNkustFVL7xoq7VE7Ge0+n4CbdHHBb82UeGM9wUjbNdr9FqhzbXc42Ud3aCNz5sc5bz3M8Q4dWn3IJrREQEREBEXDNUU8A3ppo4x3vcGj4oOZFhn6i0/GcPvNA09xqIx+K+N1Jp1/zb1bz5VEZ/FBmkXShuVvnx2NbTyZ5bkjXfcV3UBERAREQEWIvd7tdittRcblUtgpoW5c93Mno1o6k9AFV24ay2g7UbhNbNMQyUNqa7dll3uzO6es0gzjP1G/FBP2odpWitPPfFX3mHt25BgizNICOjgzO6fPCjCs9I/S0bsUtnuMw+s/s4/sw5y7+mtgGlLcxkl4kludRzcCTFCD4Nacn3nj3KWKLSGlaFgZSWC3RAdW08eT5nGSghOm9JLTjnAVNjuEbe+N0ch+wlqkOw7XNA3t7IobwynmdyiqgYTnu3neyT4Arb6rS+m6thZU2O3zNPR9PG77woz1FsJ0Rdo3uo4JLbUEHD4HEx5/WjdkY8BhBM4IIBByDyK/Sp96xtK2Q1MbahxuViLw0ZLnQ4PRpPGF/hyPirL6S1hZdWWptfbJsgHEsTsCSF/1XjjjwPIoNqREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQRhtS19Ho2w9pDuuuNVvR0cZ4gED2pHD6rc+84CoJV1dTW1M1VUzPlnmeXySPOXOc45JJ7yt82o6qfqfWNxqmyZpYHmnpRnI7KM43h+0cu96jlAREQEREBERBbvYZtJlrms0xdZy6eOP+ISuPF8bBkxE97QMt8OHRWTmmhgifLNIyONgy573BrWjvJPILzBtlZW0Fxo6uic5tTDMx8JbxO+05GB18lY2n0DtS2iSsq9T3KSgoSd5kDxggdNyBuAPN2D5oJV1Ftw0LZnPihq5LjO3hu0gDmZ8ZHENx5ZUaO2zbRtRvLNMaV3WE47QRvqXN83+ywe8KWdN7HNC2IMf+TRXTj+WrMS8fBmA0eHDKlBkbI2NZGxrWtGGtAwAB0ACCq40z6Ql99qsvTqAO6GpbBgeVKCV9/gC1ZX8bprIOJ+dwlqP77m5Vq0QVei9GikA+V1TK4/q0ob97yuV3o1W3Hs6lqAfGnaf8QVnEQVak9GiPnDqt7SOW9Rg/ESBcP8BmvaDjatahpHzflJ6f+4XYVq0QVSNp9Iiwe1BXuuEbefysVRkeU4D/ALF+4duesrHMyDVGky3jjeDJKV58QJN4O92ArVLgqKanqYXwzwxyxuGHMe0Oa4eIOcoIy05tk0LfiyNtx9SnPKGsAiyfB+S0+AzlSi1zXNDmkFpGQRyIUQal2IaHvQfJT0rrbUHlJS4azPjGctx5YUSVGnNruzRsktnrn3G2NBJaxplY0d7oXZLD1Jbw7yg7O3TaVJLUT6Wtc5bFHwuErTxe7n2IPcPpd54Kr65ppZZ5ZJZXufI9xc9zjkucTkknvK4UBERAREQFk7TdrhZrlS3G31DoamB+/G9vQ9QR1B5EciFjEQejmgNaUmsdPQXGINZO09nVQg/o5QOOP1Tzae5bwqH7EtVvsWs6akkkxS3PdppQTwEhPybvPeOPIlXwQEREBEWF1Deaex2O5XSfiykp3y7ucbxaODfNx4BBBW2bXVwNTDoywb766sLWVRj+cBJ82Fp6F2cuPd5qQNm2za3aMtrXOaya5zMHrNTjOM8ezjzyYPjzKizYTYJ7vdLxrW6fKVElRJHTuP8AOP8AaleO7gd0e8K0SAiIgIiICr/tc2XNucUmo7FGYbtTntZWRZaZwzjvNx/Kt5gjmrALG3S7W20UUtbcKuKmp4xl0kjt0Dw8Seg5oIz2RbQvzvsjoKx4/KlEGtqOnatPBsoHjjDh0PmpHu98s9lpjU3O4U9LFxw6V4bvEdGg8SfAKkE17rHbR7jX7O4qveqt8RsbCDntB8oQw5AZve0N7GFKVm2F3y91IuWtL5M+Z/F0Ecnay4+q6R2Q0DuaCO4oM7f/AEh9OUjnRWa31Fwkzhsj/kIiehGQXHywFrA1ft51RxtVlNBC7k8QNiBHfv1ROfNqsBp/Quk9ONaLXaKeGQfyxbvzH99+Xe7OFtyCqY2U7X7x7V31h2bXc4zVTSY/caA37CuxD6NYed+s1W97jz3KXj9rpDn7FaREFbmejZp8D277XE+DI2/eCvrvRt079G+3AebYz+AVkEQVin9Gm3uB7HU07D036Zr/ALnNXR/gF1nbvas+sw1w+bxmpvjGX4Vq0QVSNt9IfTuTDWuuMTefykdTkeUwEh9y5qTb1qS0TsptVaVfE7kXRtfTvwOu5Lne+0K066lZQ0VdA6CspIaiF3zo5WNe0+YdkINF01tV0RqMxx0t0bDUO4CmqfkZMnoM+y4+DSVv800UEUkssjWRxtLnvccBrWjJJPQBQnqfYLo+7CSW3dpbKg8R2Xtwk+MbuXk0hQpqq07WtHWKutNVWTVVkmYGOmjJmjYwHOMkb0QPIjg05wgzVZPd9s2tjSU8kkFgoHZ3uW6zON8jrLJj2QeQ96tbZbJa7Fbae322mZBTRNw1jep6ucepPUlQlsJv+jWaegs9HUiO6Oc6WqjmAY+Z56xniHNAGABx4ZIVg0BERAREQdarpKasppqaphZLDKwskje0Oa5p5gg8wqj6msd22Q6spr9ZN+SzVUm4+EkkAHiYHn4sdzVwVgdS2Ci1FY6+01jcxVERbvYyWO5tePFp4hB2bLd6G9WqjudDJv09TEJIz1weYI6EHgR0KyqrDsHvNZbLrftGXA7slNLJLC0nk+N25K0Z6HgR7yrPICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgLVtb3R1p0hf65jsSQ0ExjPc8tw34kLaVGW2Pe/g11Fu8+yh+ztmZQefCIiAiIgIiIC3jRmgdQaxrOxt0G7AxwE9VJkRRjxPV3c0cVuuy/ZFXarfHcbl2lNaGu4OHCSoI5tjzyb3u9wV17Za7faaGChoKWOnpom7scbBgD/ADJ6nqg0TQ+yzTOkY2SwwiprwParJgC7PXsxxDB5ce8qS0RAREQEREBERAREQEREBERBEOu9j2nNUtmqadjaC5HJ9Yib7Mh/3rBjOfrDiqZaq0hftKXA0V1pDG45MUrfailaPpMd18RzHVelawl+0/aNQW2a33SkZPBJ0PNrujmnm1w6EIPMZFK20jZddNGVJnjLqm1yvxDUgcWE8mSgcndx5FRSgIiICIiDmgmkgmimicWyRva9jh0LTkFen1qrm3C10Fc0DdqaaKYY7pGh34ry7XpLs/3vzF0rvc/yRSfZ2Qwg29ERAUFekHc3UmhY6VjsGtr4o3jvYwGU/FoU6qtHpKB35G08fo+uS589wYQS7s1tTLToTTtK1uCaKOZ/7c47V2fIuW9LFWMtNktW7800cOPLcGFlUBERARFCe1HaxT6XY612rdqLzK0Dd+c2n3uTnDq8/Rb7yg2PX+0yx6MpcTOFRcJG5ho2O9o9znnjut8evRQXadHa42q10V51JVyUdpzmCMDd3mnpBGc4B+u7OfFbRs72QVFTVfnJrPfqa2Z3aspJjvYJ4h8+eZ7mch1VkwAAABgINe07pWw6ZohSWmgjgZw33Di+Qjq9x4uK2NEQEREBERAREQEREBERAX4c1rmlrgCCMEHkQv2iCAddbDrVdHPuOnXNt1wad8RNy2CRw4jAH6N3cRw8FrOkNrl605cRp3XcE0b4yGNrHtzIwcgZMfPYejx8VaRaZrPQ9i1hbjS3GHEjQewqWAdrC49WnqD1aeBQbZBPBUQxzwSskikaHMkYQ5rmniCCOYPeudU+s9/1XsgvjbPe2vqrJM8mJ7clu6TxkhJ5EfSYf+atlbblQ3Whp66hqWT007A+ORhyHA/cR1HRB30REBERBVLVbfzd2/WKui9ltwdTF/QfL5pXfdkq1qqpts47SNEhn6TEH/mOCtWgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAtV1xa3XbR9/oWN3pJaCYRjveG7zfiAtqRB5VopD2n6VfpjWNxpGx7tNM81FKcYHZSnIaP2TlvuUeICIiAp92R7Jn6jljvN4ic21Ru+SiOQapzT8Ix1PXkFhtkuzOTV9x9crmObaKWQdqeIM7xx7Jp7vrHoFemCCGnhiggibHFGwMYxoDWta0YAAHIBB9iijhjjiijayNjQ1jGgNa1oGAAByAXMiICIiAiIgIiICIiAiIgIiICIiAiIg6dbQ0lwpJ6SrgZNTzMLJI3jLXNPQhUa2qbLqnR9YayiD5rRO/EbzxdA4/wAnIf7ruqviujcLfRXOhqaKtp2TU87CyWN4yHA//wC4FB5copM2l7PazRd4LBvS26oJdSTnuHON/wCu34jiozQEREHLFFJNLHFG0ue9wa1o5kk4AXp7aKFtutNuoW4xTUsUIx3RtDfwVHNiulX37WlJUPjzS20iqmOOBe0/Jt8y7jjuBV9UBERAUHekBa3Vug/WWNyaKuhmceu67MR+LwpxWJvdpprzaLhbKn9FVU74nHmRvjG8PEcwg1fZhdmXbQenqgOy5lGyCTv3qf5I58Tu5W/Kq+xK+VGndQXjRN2PZy+sPfT55dswYe0E9HtAc3y8VahARFG20vaBSaMsplbuyXCoDm0cB+t1kcPqtz7+SDXtrG1Bmlqb8l2tzZLzUM9kD2hTtdye4dXH6LfeVh9lOyp9te3Ueo2umu0zjLFFL7RgL+O+/POU/DzWM2RbPKurqvz01LvTVtS/tqSOXiQXce3eD1P0B0HFWVQEREBERAREQEREBERAREQEREBERAREQYDUmm7TqW1T22504khkGQRwfG4cnsPRwVW7Xc9Q7GtUG2XLtKmxVchcx7Rwc3l2sY6Pb9NvX7FcNaxqzStq1VZqi2XCPLH8Y5APbikHJ7D3j4jggzdFW0lfSU9XSTsmp5mNfFIw5a5ruIIXcVR9D6muuzLU82ktSPxbpZcwTnO5Hvn2ZWE/yb/pDoferbAhwBByDxBCD9Ii1zVWo6LTVguF2qiN2CMljORkkPBjB4uKCumpXDUnpAWaji9pludThxHEfxYGpdn3nB8Va5Vk2CWKsray96xuILpqyWSKFxHzi92/K8eGcAe8KzaAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiCLtqmgGaysO5AGtuNJvSUjzwDifnROPc7HPocKgtVTVFJUzU1TC+KaJ7mSRvGHNc04IIPIhepaiDaTsmtesGOrKZzKS7Nbhs+PYmA5NlA+DhxHigoUt10Joyv1hf4LdT5ZEPbqp8ZEUQPE+JPJo71jbrpa92m/OsdVSH1/tGRtiY4PLzJjc3S3Od7PBXv2b6HptG6eipAGurJsSVsw+lJj5oP1W8h9vVBt1ms9vstspLdQQiKmp4wyNg+JJ6k8yepWUREBERAREQEREBERAREQEREBERAREQEREBERBruqNNW3U9lqrVcI8xSty14+dG8fNe3uI/5Lzw1Tpq5aYvdXaq9mJIjlrwPZkjPzXt8D/yXpioj2ubPmausRmpYx+VKJrn0xHORvN0RPj9HxQUHWQtltrrrX01DQ07pqmeQMjjbzcT9wHU9Fl9MaTvWp7sLXbYA6oALpN9wY2NjSAXOJ6DPIcVd3Z3swtGi6YygipuUrMTVThjA6sjH0W9/U9UGT2daJptG6dhoGlr6qQ9rVzD6cpHIfqt5D7VvqIgIiICIiCvm2bZ9WV/Y6psTXi50Qa6ZsXB8jIuLZGY+mzHvHktl2X7UaHV9DHSVcjIbvCz5WLkJgP5SPv8AEdFLyr7tB2MC41br5peYUVzD+1dE1xjjkeOO+xw+Y/4E9yCZtRagt2nbPWXSvk3YIGZIHznuPBrGjqXHgFWHQunrltO1bVas1BHm3QShsMB4seWcWwtB5sZzd3n3rToLjrnaddrTpe4VbXMo5HmolY0YDWHddLIWndcWjg0jmT4q7FntNBZrZSW2hhEdNTxhkbR3DqT1J5k9SgyIAAAA4L9IiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgjbaXoCl1nY3RNDWXCnDn0cx6O6sd+q7HHu5qO9i+vKovk0dfS6Ovoy5lKZODnNj4Ohdn6TMcPDyVjVW3bdoipjdDrOy70VbROY6rMfBxawjcmHizk7w8kFha+4UVuo56ytqI4KeFhdJK87rWgd5VSL1dLxtk1dBarY2SCx0T998hGMN5GZ4+u7kxv/NdS1UmvNslWZK+5Q09qpZGtkbHgMa7GfZjBJc8j6TuHcrWaY0tZtL2qK3Wun7OJvF7zxkkd1e89Sf8A2QZK1WujtFtpLfRRCOnpomxxsHQDvPUnqVkURAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAWsav1NR6X09X3apwRDH8nHnBkldwYweZ59w4rZ1U/atcKvW2vbToq2yHsaeYesOHECUjL3nvETPjkIMhsT0vWXq6V+ur1mWaaaQUhcOb3cHygdA35re7irQLH2u20dqt1Jb6OMR09NC2KNvc1owM95PUrIICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIKnbU7LW6F1nbtbWZm7DPUZqYxwb2xHttdj6Mrc+/Ks3ZLxRXu0UNzon71PUwtkYeozzafEHgR3rransFHqOxXC01Y+TqYi3exksdza8eLTxCr7sOv1ZZrzd9EXU7ksUsj6ZpPASR8JGN7w4DeHvKC0KIiAiIgIiIChfbVrg6b02aGkl3bhcQ6OMg8Y4uT5PA8cDxOeimOWSOKN8kjg1jGlznE4AA4kk9wVSdLwP2n7Vay91LHPtVtc10THDgWMJEMZB+sQXuHmEEubHdCjS2m2VFVFu3Gva2WoyOMbebIvDAOT4lS+iICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgLilijmjfFIxr2PaWva4ZDgRggg8wVyogp/AZtkW04xOc4WO5Y4nJAhc7gT+tC48eu75q3rXNc0OaQQRkEciFGG1vRo1TpKpbDFvV1HmopMDiS0e1GP2x078LB7DdYG+6VFuqZN6ste7Ecni+E/o3e7G6fJBNyIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiDXNWX+HTmnLpdpcEU0DnMaeT5D7LG+9xAUF+j/p6aZt41bXkyVFZM+KGR3Mje3pX/vO4e4r56Q16nlisOmqTLpqubt5GDmcHs42+TnE/Yp70zZILDYLXaocbtLTsjJH0nAZc7952SgzqIiAiIgL8Oc1rS5xAAGSTyAXxzmsa573BrWgkknAAHMkqkO1XaxW6lrKi12qd8VnjcWktJBqiObn/qfVb7ygsPqDbXoOyyvhFbJXTNOHMpGiQA/tktafcStOj9JHTBkw+y3JrM/OHZuP2bw+9U3RB6J6Y2naM1PI2GgubWVLuVNOOylPg0Hg4/skqQV5XNc5rg5pIIOQRzBVtNjO1mpuFRDpy+1Bknc3FFVvPtPIH6KQ9XfVPXkgs6iIgIiICIiAiKpG2La3VyVdTp6w1TooYSY6yqjOHSPHAxsI5NHJx6nhyQTfqXavojTkskFVcu2qWHDqemb2r2kdHEYa0+BIKj4+khpXtMCz3Pc+tiLP2b/4qmiIPQfTe13Q2oJY4ILl6tUPOGwVTexcSeQB4tJPcDlSavKtWQ2QbXKqgq6WwXyqdLRSubHTVEhy6Bx4Na4nmw8hn5vkguIiIgIiICqttutdTp3VNi1rbm7rzMxk+OAM0PFu94PYC0+AVqVpO0PTo1Ho+724M3pXQGSn7+2i9tmPMjB8Cg2W03KlutsobhTO3oaqBksZ8HjIB8Rnisiq/wDo96hNfpWqtMr8yW2o9gH+Zmy5v2ODlYBAREQEREEK7dNUmy6NfRQybtTdHGnbg8RCBmU+RGGnzWa2R6VGm9F0Ecke7VVY9aqc8w6Qey0/stwCO/KhvVw/PjbZbrL8+itzmslHNpEQ7WbPmfYKtogIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICqNUt/g320xys+Ttd1dkjk1sdS7Dh4COQZ8lblQJ6QOnRcdIxXWNmZrbOHEjn2MxDHD3HBQT2i0XZtqE6h0VZq9796bseynJ59rD7DifF2M+9b0gIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiLr1dTHS0tRUSHDIonSO8mDJ+5BVaAfnb6QUrz7dPapCQOe76mN0f8U5VsVVn0dqZ9ZcdV3ycZlkdHGHd5lc6ST4gK0yAiIgIiIIQ266t/IukzboJN2quhdEMc2wN/SH35DfeqNKSdqurPzo1jXVMUm9SU59WpcHgY4ycuH7TiT5KNkBERAXYp556aeGeGR0csT2vje04LXNOQQe8FddEHplpK9i/aatF1wA6qpWPeByEmMPA8A4FbEon2Jdp/BnYt/lmp3fLt3qWEBERAREQaLtJ1FJp3Rd4uML92cRCKAjmJJTuNcPFuc+5edDiXEknJPEkq7npC9p+YUW7y/KcG/5bj/xwqQICIiAiIg9A9kWrTqbR1JJNJvVlH/FqnJ4uLB7Lz+03GT35UoqiWw/Vn5C1hFRzSbtJcw2nkyeAlz8k77Tu+9XtQEREBERBU7RQ/NPbnebN82nrjM2NvJoEg9Zj+weyFbFVR2x4se07SN+b7LXdg6Q/WNPL7X2tcAVa5AREQF07hWQ0NDV1kxxFTwvlef1Y27x+5dxRntguRt+zq/yNdh00Ladvj2zwxw/qkoIl9H6hmuV41RqaqGZZX9kHd75ndrJ9w+1WmUObCbYKLZ5QS7uHVlRPUO/r9mPgwKY0BERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAWIvtriu9muVtlxuVVLJCSem+3APuysuiCsfo6XOWKPUVhn9l9PO2drDzBPycg9xaFZxVR0yBYPSDvFC32WVzqgY6YmjFUPiFa5AREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBabtCqvVNDanmBwfyZUNB7i9hYPvW5KNdsMnZ7NtRnvhjH9aVo/FBqHo8Ugh0PVTEe1Pc5XZ8GsY0fEFTyof2FR7uza1u+vNUn/iuH4KYEBERAWhbTrzLZtB6grInFsnq3ZRuHNrp3CIEeI3srfVE+22mkqNm173ASYzTyEDubK3P2DigoGiIgIiIC7FPBNUzwwQxuklle1kbBzc5xwAPErrqedgmk/yvqh92njzTWtoe3PJ07+DB+7xd4HCC3WlLK2w6btFqBBNLSsjeRyL8ZcR5uJK2FEQEREBERBou0nTsmotF3m3xN3pzD2sAHMyxHfa0eLsY9685yCCvVJUG2y6T/N3WVU+GPdpLhmpgxyaXH5Rg8ndOgIQRIiIgIiIORj3se17HFrmkFpBwQRyIXpdpO7OvOmbLcnH26mihkkx9dzRvfHK8zV6M7MqaSm0BpmOTg40Eb+PdJ7Y+BQb2iIgIiIK0ekpSB9n09V44xVc0Wf6Vgd/gVg7JVGsstrqic9vRwy5799gd+KhX0i497Q9C76t3hP2xSBSjoKTtND6Wd/8AaKQfZE0INtREQFAXpFVXZaJooQeM10jBHe1sb3H4gKfVWr0lJMWTT7O+slP9VmPxQTNoGkFJojTMIGCLXTOcP1nxhx+JW3rE2JnZ2O1M+rRQD7GALLICIiAiIgIiICqvtR213KiulTZdNyMi9XeY6itLQ9xkHBzIw7IAbyJxnPJWmccNce4ZXllLLJNJJLI4ue9xc5x5kk5J96CSLZtf2hW+qbOL7NUDey6KoAljcO4g8QPIhXP0Brai1nYY7jCzspmO7Kpgzns5AM8D1ac5BXnGrS+jTLJ2+qIt47m5Sux0zl4ygteiIgIiICIiAqe7TdtV5mutXatO1RpaSnkdHJVMx2kz2nDi13HdaDyI4nnlW1uMj4rfWSMOHNgkc09xDSQvLokkoN+tO1DXlrqm1EWoa2bDsujqZXTxuHUESE4z3jBV3NAa0pdZaeiuUcYima4xVMOc9nK0AnHgQchecath6NEjzBqqMuO6JKMgdASJAT78ILSIiICIiAiIgIiIKqa9H5O286UqRw9Z9RJP7cjoD8ArVqqu2r5LaXoeccx6v/3KnP4q1SAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICjXbAwv2b6jAGfkYz/VlafwUlLTdoNIavQ2p4QMuNsqHAd5YwuA+CDUdhUgds3tjQfmT1IP8Aak/ipgUCejvVibQ9VDnjBc5W48HMY4H4lT2gIiICxt2tlNdrXXW6oGYaqCSGTHPde3dJHiM8FkkQeYuoLHXWC8V1rrY92emlLHdA4cw4eDhxCwqv9tM2X0GtaRs0T2090gbiGoI9l7efZyY5t7jzCpPqLSOotNVLqe7W2WA72GyEZjf4seOBQayiLKWuz3W8VTKW20M9VM7kyJhefM45DvJQdGKKSaRkUbHPe9wa1rRkkk4AAHMleh+zXSQ0ppKgt8jQKp47arI6zScxnrugBvuUd7K9jTdPTRXm+9nJcWjMFO0hzKcn6RPJz/gOisGgIi1TXLrm3R2oDbd/1sUE3Zbnz87vHdx9LHLxQcFdtB0TQVMlNU6ioGTRuw9naglpHMHGcEdQur/Chs+/6TUH9ovOjmviD0ntuutHXWqZS0N/oZp38GRNlAc7waDjJ8AttXllCZhNEYS8Sh43CzO9vZ4buOvcvTqzGtNotprh/G/VYfWP6XcG/wDFBk1Eu2PRz9T6SlNNFv11A41FOAMueAPbjH7Q4gdSApaRB5WL4rbbUNiUlfU1F501G3tpCX1FDkND3HiXxE8AT1afcqrVtBW2+pfTVlLNTzMOHRSsLHDzDsIOkiLb9L6I1LqqpbDarfI9m9h9Q4FsMffvPPDh3DJ8EHHozTFVqnUdBaqdrsSyAzPH8nC3i958hy8eC9I4IIqeCKCJgbHGxrGNHINaMADyUf7O9nVs0VbXRxuE9dOAaqqIwXY5MYOjB8eZUjICIiAiIggH0i3huiKBvV13i+EUhUo6CYWaI0s0jB/JFIT74mlQr6SlWGWfT1JnjLVzS4/omBv+NWDslIaKy2ulcMGCjhiI8WMDfwQZRERAVbPSTYTYrBJjg2tkbn9pmfwVk1AvpEUhm0NSzAfoLnE8n9VzHs+8hBMdgkEtitEg4h1FA4e9gKy603Z5Vis0NpmYHP8AqynYT4xsDD8QtyQEREBERAREQfCAQQV5jX+zVVivVwtdUwtlpp3RnPDeAPBw8HDiF6dKPNa7NNM6xDJK+GSKqjbusqoCGyBv1XZBDh5jyQedyt96ONkqqa13q7SsLYquSKKDIxvCHeLnDvGXY9xWQtXo66Xpapstdcaysja7Ih9mJrvBxbkkeRCn2kpKWipoaamhZFBEwMjjYA1rWjkAByCDsrr1FTTUlPLUVE0cUMbS6SSRwa1rRzJJ4ALsKCvSCiucmhmGlDzA2vidVhv83uuwXfqh2PfhBtr9rmzlji06kp8g44NkI+0NOV8/hf2cf9I4P7OX/wDleeiIPSuw600tqKSSK03inqZGDLo2kteB37rsHHitpXnTswjucmvdOfk8P7RtdG6Qt6Qg/K58NzOV6LIOGohbPBNC75sjHMPk4YXmRfLPW2S711srIyyemmdG4HhnHJw8HDiD3L09Wh6w2c6W1eGOudK4VDG7rKqF25K0d2cEOHcCCg851c/0eNP1dv05cbnURuYLjOzsQRgmKEEB/kS448lk7PsA0Pb6ttRUPra7cdlsU72iPhyyGNaT5E48FNscbImMjjY1jGNDWtaMBoHAAAcgEHKiIgIiICIiAiIgqrtn+V2naHgHFx9W4ft1OB9ytUqqa4/1lt90vTN4ml9SyP6J7qg/Aq1aAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIC69XTx1VLUU8g9iWN0bvJ4wfvXYRBVr0d6qSiuOq7FOcSxvjkDe4xOdFJ8SFaVVMrX/AJkbeWVLzuUd2dlzuQ3av2XEnwlGT4K2aAiIgIiIC4ZoYZ4nxTRMkY4Ycx4DmkeIK5kQak/QmiXydo7S9pLs5J9Ui4nx9nitho6ChoIRDR0kNPGOTImNjb9jcLuIgIiICIiDRq3ZtoSvqZKmo05Rulkdl7g0s3ieZIaQMnqVVWx6csdRtvmsktBG63CvrYxTHO7uxxPc0d/AgK8apnpx3/xEz/8A7W4j/hSBBZm17PdFWmrjq6GwUcU8ZyyTd3nMPe3ezg+IW5oiAiIgLHXC0Wq5xiO4W+lqmDk2eJsoHucCsiiDUYdA6Igk7SPTFqDhxB9VjOPLI4Lao444mNZGxrWNGGtaMADuAC5EQEREBERARF+XODQSSAAMklBVTbKfy5tL0hYGe01vYiQD6JqZcOz5NaCrWqpuz0nWW2S96kPtUtF2j4XdMEdhCPAloLvMK2SAiIgKONrVsNy2eaiha3Lo6cTt8OwcJD8GlSOuCpp4qmnmp5m70csbmPaerXDBHvQQ/sHugrdn1LBvZdRVM0Du/Bd2o+D1M6qlsTqpdN631JpGsfhz3u7HPDekpieX7bDveQVrUBERAREQEREBERAREQFxSRxyxvjkYHscC1zXDIIPAgg8wVyogjq87PtDMtlymbpm2te2mlcHNgY3BDSQRgcFXbYDp6xXus1A2622mqxFDTmMTMD90uLs4zyzhW4vxxY7sf8AqU/9wqr3o0n/AFlqUf8AV6f+85BZq0aa0/ZO0NrtNJSGQYe6GJrHOHcSBkjwWdREBERAREQEREBERAREQERa3q+/Rae01drq8gGmp3OjB5OkPssb73EBBXbSR/ODb/e7i32o6E1BDumImCkH25yrWqt/o7WOSO03i+zgmStqBFG53Msi4udn9ZzuPkrIICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIIJ286SfedMMutNHmptZdI7A4ugf8/8Aq4DvIFbZss1kzVelKWeSQGupgIKwdd9o4P8AJ44+eQpGexkjHMe0Oa4EOaRkEHmD4FVBuMFw2O6+bXUsUktiuBILByMZOTHx+nHzaeo96C4SLoWy50N1oKauoahk1NPGHxyNPAg/cR1HRd9AREQEREBERAREQERQ1tPqNqMlXQ2/SVLu088J7arYWB7X5wWlzzhgAwQefcgkO/6r07p2n7a7XOCmaRlrXOy9/wCywZc73BUpsusLNS7XX6lmfI23uuVXLv7hLhHM17WktHH6QypgsHo/mon9f1beZqyoed58MT3HeP68r/ad44A81Ls2zTQcttFuOnKIQAcC1m7KD39oPbz45QbDZdQ2S+0wqbVcYKqLhkxuBLc9HDm0+BWaVX71sGudrqvyjo2+zQTNJLYZXmN48Gysx9hHmVJezCs2izU1xp9X0e46ndG2nncGB8vPez2ZIcBgYd96CVUREBERAREQEREBERAUM7a9ZN09pSWiglxXXJroIgDxbERiR/2HA8SpNv19ttgtVVc7jOIqeFmXHq49GtHVx5AKrujbVctqWup9T3iEttVHIBFCeLCWHMcAzzAzvPPX3oJg2NaRdpzR0DqiPdrLgRUzgji0OHsMPk3iR0JKltEQEREBERBVrbZaK7T2pbNri1tw5ssbKggcBLH8wu8HtG6fJWK09faHUFlobrRPzDUxB4HVp5OYfFp4Ffu+2WhvtorbXXR79PUxFjwOY6hw7i08R4qreidQXDZbq2r0tqB5/JlRKHRTngxhdwbO39R2MP7iPBBbxF+Gua9rXNcCCAQQcgg9Qv2gIiICIiAiIgIiICIq5a10/th1PqOut1NUsobGHARSNlEbHxkfT3MyOJ6tPBBvOvdpOj7LbblQz3NktZJTyxNpoPlXhzmlo38cG4z1IVbdietrDpW7XP8AK80kMdXDGxkoYXtaWOJ9vd4gHPMAqctK7BdJWjs57mX3SoHHEo3IAfCMZz+8SPBb5ftnWjL9TNgrbLTjcbuxyQtEMjAOQa5mOA6A8EG0W66W26UrKq31kFTA7lJE8Pb5ZGePgsgqq3LYpq/TVU+4aKv0riOPYPf2MpA5NJ+Y8eDsBT7omXVMunKJ+pYWR3L2u1Dd3iAfZLgzLQ4jmAg21ERAREQEREBERAREQFVrbfqCpv17tOiLQe0mdURuqQOXav4RsJ6BoO873dylzaVtAo9GWV0oLJLhO0to4Cebusjh9RvXv5KPNieh6xjp9Y3vffX1286m7T5wZLxdMc/Sf08PNBOOnLJS2Cx260036KlgbGHYxvEcXOPi4kkrNoiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAsBqTTlq1LaKm13KHfglHAjg5jxyew9HDos+iCnduumqdjN+dbrjG+ssVTIXMcwcHD68WfmyD6TDz+KtXY79ab/bobhbKtlRTycnNPEHq1w5tcOoK/d5strvlumt9zpI6imlGHMcOR6EHmCOhHFVgu+zvXOzq4zXjR1XNVUXOWnxvyBg+jLGOEjR9YcR4ILaooI0dt205eBHTXkC11vIuec07z4PPzPJ3LvU5RSxTRskje17HAFrmkEOB5EEcwg5UREBERAREQEREBERAREQEREBERAREQERcFRUU9NBJPUTMiiY3L5HuDWtA6kngAg51r2pNT2XTNtfX3WrbFEMhjeb5HfVY3qT/AO6h7WG3qy28votOQ/lOsJ3Gy4Iga48BjGDIfAYHitUsGyzVutrky+65rJ44TxZSk7srm8w0NHCJnhzQYcN1Vtp1C1zg+i0/SS+YYPD68zh7mhWws1nt9ktlLbrfA2GmgZuxsH2kk9STxJ6rmt1toLXRQUVDTRwU8Ld2OJgw1o/zPUrvoCIiAiIgIiICj/aDoC2a0tBppyIquLLqSpAyY3HmD3sd1CkBEFStGbQb5s9uX5q6xhlFJEQ2Co4vMLCcAtP04j0xxHwVq6SspK2miqaSeOaCVodHLG4Oa4HqCOa1/VmjbDqy3GiutNvgZMUzfZlicerHdPEcj1VaprNtK2SVMtTbJTcbIX70jQ0ujA75GDjG79YcO8oLfoog0ftn0jqMRQzzi3VrsAwVDgGOP6knAHwBwfBS6CCMjiCg/SIiAiIgIiICIiAiIgIiICIiAiIgIiICIsJe9R2OwUpqrrcYKWPjgvd7TsdGtGS4+ACDNqMNoW0+yaNpnRlzam5PbmGja7iM8nSkfNb8T0UT6h203/UdWbNoa11Bkk4etFm9KRyJY3iGD9Z3wWxaE2JQ0dS28armFfcXP7TsHOMkbHnjvSF36R3w80Gr6D2f3vW95Gr9Y7z4HuD6emeMdsB832fowjoPpK1YAaAAMAcgvuAF9QEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQRtq/ZXpDVXaTVNH6vWO/+rp8MkJ73jiHe8Z8VCr9nW1jQsj5tLXd1bSA5MLCAT370MuWk+LSSrZogq5bdv8AdbZOKPVWmZYZm/PdCHRPHnFL/mFK1m2v7PrsGhl7jp5DzjqgYCP3nez9hXDtS1hpfT1mLLtRU1wqZmn1ahlY1++eW+4OB3WDqfsVCKqoNTUTT9lFF2jy7s4m7jG5PJo6AdEHqDTVdLVxCWmqIpozyfG4PafeMrsry2pa2so5RLS1M0Mg+nG8sP2twt1oNqW0Kgx2Gpa1wHITOE//AIocg9FEVGaP0gNoNOB2slBU4/nafGf7MsWx03pJagbj1ixUEnf2b5I/vLkFw0VVYfSY/ntK+9lZ+BjWRj9JW0n5+nKpvlOx33gILMoq3t9JPTp+dYq8eToz+IXIPSR0x1styHl2Z/xILGIq5O9JLTX0bJcT5mMf4iurJ6SlnH6PT1W79qZjfuBQWXRVXm9Jdv8AI6VPm+sx8BGsLU+knqB2fVrDQR93aPkk+4tQXCRUYrNv+0Goz2UlDTZ/mqfOP7QvWoXDahtAuAPb6lrQDzELhAP+EGoPQyrraOiiMtVUwwRjm+V4Y0e92FG952ybPbSHA3htVIP5OkaZs+Th7HxVBqmrqquUy1NRLNIeb5Hl7vtOV2bVXMoLhS1b6OCqZE8OdTzt3o5B1a4eKCzdft61BeJ3Uek9MySSHk+Rrp5MHr2cXAY7ySF1Ydl207WszKnV17dS0+d4QOcJHD9mKPDG+ec+CnPZ7qbS9/scc1ip4KVseBPRxsbGYH45FrcZB6O6rfkGgaS2aaS0mGvoKHtKoDBq58STHvweAb+6At/REBERAREQEREBERAREQF8wCvqIIf1bsV0dqF0k8MBt1W7JM1MAGOJ6vj+afHGD4qKhpTbToE/6krnXKgZyhjPat3e7sZPaaT+p9qtqiCsNq9Id9NL6rqXTs1PM04kdT5BB8YpcEf1lK1o2tbP7sGiK/QQvP0KnMBB7syYafcVG22TX9oO9pq3W6lud0kd2bnPhbOKdzuAawEHMp6AclEN/wBntm0hpCOo1DUTm/VvGkooHtDYWjmZSQ7IGeOOvAd6C9FPU01TEJaeeOWM8nscHNPvGVzqlWkNimsLhZYLvBdxbJ5/ahhd2jHmP6L3OZxbnoMcltP5pekFZ/8AY7+awDl/Gmy/+aAQWsRVU/On0hrbwqbEarHP+Kskz/2chff4ZtqNJ/t+h8Y5/wAVqYf7xcgtUiqr/pGXWD/atH4xz/jDo/70ZXOz0mKc/P0rIPKrB++MILRoqxt9Ja29dN1A8qhp/wAK5B6Sloxx07V5/pmf5ILMIqxu9JW2j5umqg+dQ0f4Suq/0l2HhFpNzj0zWY+AjKC0yKqv8P8Aqmq/2LRmc8vall/utavn8J+2uv4Uei+zaeT/AFGoP/ee7dQWrRVU7X0kLrwbGaSM8+FLDj+tl6+fwSbWbz/851huxu5xmpmmx+4A1vxQWNuuqdN2cO/KN5oqYj6MkzWv9zc5Kiy97f8AQ9AHNovWrhIOXZRmOPPi6TdOPEAqtjdHW3Tut22TWTqmGkecMq6dwY0h5wyXL2uyz63Ue5bNNZarZRqyCpuFpprtZ5ziGeSFj95vMFhdnclb3cig21+0va1rMmLTFhdR07jjt2N3yPAzS4YPcAVk7LsEuFxqhcNY36aomcQXwxPdI4+DpZPiAPIqw1ivVqvlrprhbKhk1LK32C3hjHNpHQjqFmUGDsWm7Fp+j9VtNuhpYuG9uD2nkdXuOS4+JKziIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICi7aTtNtmi6Ixs3Ki6TMzT02eDRy7STHJo6Dmeix21DatQ6Qpn0VEY6i7yM9iLm2AHk+THXub1VHLjca651tRW11TJPUTPL5JXnJcT+HcOiDnvN5ud7uVRcbjUvnqZnZe93wAHQDoOixK/QBJAAyVLVVsR2iQUsNQy1xzh8bXlkczN9m8M7rmvLTkdQMoIjRbFcdJ6nte8a+x19O0fSkge1vudjBWuoCIiAiIgIiICIiAiIgIi+oPiLZLbpHVV03TQ2GvnaeT2QPLf62MBbhLsb1/T2qsuNRa2wx08LpXRulY6RzWjJ3WsLuIHQ4QabpnU930xdoblbKgxzM4OaeLJGHmx46tP/sr6aC2gWfWdsE9K4RVcQHrNI52XRk9R3sPQrzpWZsV9ulgudPcbbUuhqIjkOHIjq1w6tPUIPTtFGezraVataUGBuwXGFgNTSk+7fjzzYftHIqTEBERAREQEREBERAREQERfMgIPqrltN2sVDao6Y0kXT3KV/Yy1EPtGNx4dnFjm/vP0fNY/aLtSuF4r/zT0ZvzzzvMU1VDxLj1ZCegH0n/AGKQdmWy2g0dSiqqQyou0rMSz/RiB5xxZ6d7uZQa1ovQVo2c2Sq1RqN7ZbjHCZHu+cIN7h2ceecjicF3ecBaPoCw1+0vWNZq2/R5oKeYCGA8WOc3iyEZ5sYDl3efMrvbX7zXat1da9DWl+WsmaakjiDM4Z9rHNsTeJ8c9ysjp+x0Ngs1DaqJm7BTRBje9x5lzvFx4lBmkREBERAXA+mp5Pnwxu82grnRB0TbLaedDTnzjb/kuP8AI1oJz+TaTPf2LP8AJZJEHRba7a35tDTjyjaPwXaZFFGPYja3yAH3LkRAREQEREEc7StB0usrA+nAayugDpKKY9H44scfqu5H3FRNsqv1NqC112z/AFVT9pNTteyBk3BxZGcGPPMPiI9k88eSs+qu7bNN1dju9u11Zvkpo54xVFo4CRvBkhHc75rvd3oNcqqTVWxfUPrVKX1tgqpAHA8GvH1X4+ZK0cncj8FaXTepbRqa1QXK11AkhfwcDwfG8c2PHRwWPs1ws2uNJU1TJTxzUldT4ngf7Qa4cHsPi1w4H3hVtvVh1Rsev35Zsr5KqyTvDZY3kluCeEc2ORGfYeguEi1TSGr7Nq21MuFtmyOAmhd+khf9V4+48itrQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQFBG1Xa9T6aZNabRIya7Obh7+DmUoPV3e/ub05lYXavtmjtfrFk07O19ZxZU1jTlsHQtjPV/efo+aqDJI+R75JHue5ziXOcckk8SSTzJQclVVVFXUTVFTM+WaV5fJI8lznOPEkk8yV1kRBMexPSY1BrKGonj3qS2tFTLkZDpM4jafN3HHcCr4qEtg2nha9Ex1r2YmuUzp3E8xGw7jB5cCR5qbUBYev0/Ybln160UNTnn20DJP7wKzCII5rNkuzqsz2um6Zuf5ovh/8NzVrdTsC2eTZ7OmrIP6Oocf7+8pqRBXub0cdHO4w3S6s/afE4f3AsdJ6NdkP6PUFY39qJjvuwrKogrC70aaA/N1NOPOmaf8AEFx/6NFN/wBKpf8Asg/9RWiRBV8ejRR9dUTe6lA/xrsx+jXZx+k1DVu/ZhY37yVZdEFeoPRw0g39Ndbq8/quiYPiwrN02wLZ5DjtKesn/pKgjP8AU3VNSII5o9k2zqjx2Wm6V2P50vm/8QuW30NgsVux6jaaKmxy7GBkf90BZdEBfkgEEEZB5hfpEHnftQ0p+a+sbhRxx7tLMfWKTu7KU/NH7JBb7lHauT6ROnxVaet96jZ8pQ1HZyH/AHU/DJ8nAY81TZBkbXdK+019PXUFS+CpgfvRyMOCD+IPUdVeXZjtUoNYUzaSqLKe7RszJDybMBzfFn4t5hUJXapKupo6mGppZnxTxPD45GEtc1w5EEcig9SkUFbK9r9LqaOK1Xd7Ibs0YY7g1lUB1b3P729eYU6oCIiAiIgIiICIutV1dLRU01TVTMhgiYXySPcGta0cySeQQcskjI2Pke8NY0EucTgADiSSeQCqtrvaPeNa3Q6S0Y2SSGUllRVM9kzAcHYP0Yh9J3XyXT1VrTUW0+8nTOlI3stm98vOcs7VoPGSU/RjHRvM/BT9oTQNn0ZbBTUjO0qZADU1bhh8rh9zR0agx2zrZratFUGW7s9ymaBU1RHv3I88mD7TzK2zVV+g09p66XaYAtpadz2tPDeeeDG/vOIC2BVt9Im9yMtllsNOSZK2oM0jG8y2L2Wtx+s53DyQdfYDp+eqfeNX3DMlRVTPige7mS478sn7zjjPgVZpa7pSxRaf03abTGB/FqZrHkcnSHi93vcSVsSAiIgIiICIiAiIgIiICIiAiIgLFXq0Ud6tFdbKtu9DVQuif3jeHAjxB4jxWVRBVrYbdKuw6jv+i7gcPZLJJCDy7WL2XhveHNAcPAKzlVSU1ZTTU1TCyWGVhZJG9oc1zTwIIPMFVY2uRP0ntL05qunaWsncx02PpOgIZIP3o3AK1kb2SMa9jg5rmgtcORB4ghBUnVWjtRbLr1+c2lpJJLWXYnhOXiJpPGOUfSjPR3MeasDobXlm1laxVUb+zqIwBU0rjl8Tj97T0d1W6SRxysfHIxr2PaWua4ZDgeBBB5gqquuNnV60PdDqzRj5GQREvnpmZcYW83cPpRHqOiC16KNNne0q060oQGlsFxiYDUUhPHu348/OYftHVSWgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiiLWu2PS2l+1popPyhcG5Hq8DhusPdI/iG+QyfBBKVXW0lDSzVVXURwwRNLpJZHBrWgdSTyVSdpe3Ca5NntWmpJIaU5bNW8WSSjqIxza09/M+CibWW0LUur6jeuNVu07XZipIsthZ44+kfE5K0VAREQF2KanlqaiGnibvSSyNYwd7nHAC663/ZfbxcdoGmoCMgVrZiPCAGX/Cg9BbVb4bZbKGghGI6anjhZ5RtDR9yyCIgIiICIiAiIgIiICIiAiIgIiICIiDV9aWgXrSd8t25vOnopBGP940bzD7nALzTXqovMzVdvFs1PfKEDDae4VEbf2WvIHwQa8iIg5WPfG9r2OLXNdlrgcEEciD0IVqNmu3Vm7DatVTYIAbFcT17hP4/r/b3qqSIPU+KWKaNksUjZI3tDmPaQ5rgeIII5grlXnrofajqXR72xU83rNBvZfRzElnHmWHmw+XDvCuBovappXVrWRU9R6tXEcaOchryf1DyePLj3hBJSIiAi69TU01JBJUVM8cUMbd58kjgxjQOpJwAFXrV23mkjmNt0nSOuFY9242oLHGMOPD5Ng9p57uQ80E0am1ZYtL0Dq27VjYmcRGwcZJSPosbzJ+A6qsFVcNbbZbr6pRRuoLDBKN8nJYMfSkIx2knc0cB8VndObHtR6nuDb5ryvmJfgik3/lXDmGuI4Rt/Vbx8lZm326httHDR0NLHBTxN3Y4o2hrWjyHf1KDB6S0hZtJ2plBbYd0cDNM7jJM/6zz9w5BbUiICqhfB+c/pA26jPtwW50QPdimYag5/fOFa9VT2ND8r7TdZXt3tD5ct8PWJ8jHk1uEFrEREBERAREQEREBERAREQEREBERAREQQjt9tArtByVYZl9BVRTZ67rz2Th5e0CfJbbssu35W0Bp+oLsvZSiB+eeYD2XHxO7lZjW9vFy0hqCjxky26cM/aDCW/EKJPRzrzNpG40bjk01xcW+DZWNIH2goLCL4QDwK+ogrTtA2RV1FX/nNolz6esieZZKOI7pz1dB59Wcj07lnNnm2mgvJjteodyhujT2e+72IpnDhjj8x/e08M8u5T0on1/slsGr2yVLAKO544VTG8HkchK3hvDx5oJYRVCotXbR9llTFbtQUb6+1A7sMhcXDA/mZemPqO+CsTpPXumdWwB9rrQZg3MlLJ7EzPNvUeIyEG6IiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIvy5oc0tPIjBQUm2mbY7ve6yrttmqX01rY50e/Gd2SpA4FxcOIYejRzHNQMtk1Vpyv01fa61VkbmuhkPZuI4SRk+y9veHBa2gIiICIiAps2BUwm2hQSEZ7CiqJB4ZAj/AMShNWB9HJgOtbk4/Rs8gHvmjQXTREQEREBERAREQEREBERAREQEREBERAXnztiphTbSdRMAwHSxSf2kTXn4legyoht4YG7Rq8j6VNTk/wBmB+CCGkREBERAXI1zmuDmkhwOQRzBXGiCzGyfbHdm3OhsV+qHVNPUSNhp6p/GWJ7jhrXu+k0nhk8R3q0WoL3SWGy191qyexpYXSOA5uI4Bo8XE4CoHs103W6h1jaaeCNxjhqI56mQDhHFE4OJJ6E4wPEq9OubBJqLSV5tMRAlqKc9lk4HaMIewE9AXNGSgrPQ2vXu2OsfW11b6jZI5iGMGTGCPoxs4b7x1c7/AJKx2kdn2l9JQhttogZy3D6uXD5n9/tdAe4YChDY9tFt1gpH6T1ETb56aokEMkw3GAvdl0chPzSHEkE8FaGKWOWNskb2vY4Atc05BB6gjmEHKiIgIiIOlcqj1W3VtRnHZU8j8/sNJ/BVu9GqmAoNTVOOMk9PHn9hrj/iU+avfuaT1E/6trqj9kTlDPo3sA0nd39TdCPsiZ/mgsQiIgIiICIiAiIgIiICIiAiIgIiICIiDjexsjHscMtc0gjvB5qrfo4udT12rqFx+aac48WOkafvVqFVbYj8ntE1tCOQ7b/u1GPxQWpREQEREHVq6SlraeSnqqeOaGRu6+KRoexw7iDkFV41dsIjbObpo+sfQ1kbt9tMZHNbvf7qTmw9wPDyVkVqWqda6c0rSunulfHG/dzHTtIdNJ4MZz9/LvKCMNk20e83W4VemNSRubdaRrt2VzQ10gjOHMkA4b7e8cwp8VVtkdJc9U7QL1raopXQ0pMoh7jJJhgYD9LcZ849+FalAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQarqnRmndVUYprtRNl3c9lK32ZYyerHDl5cj1CrXqH0crvA58liukNTHzENR8lIB3BzctcfHgrfIg857nsz15ay71nTlaQ3m+Fnbtx35i3gtMqKSqpX7lRTyRO+q9pafsK9S1+Hsa9u65ocO4jKDyuX7ALiAASTyAXqA60Wl5y63UpPeYmn8F2YaSlg/Q08Uf7DQ37kHnFZ9BayvT2NoLDWyNdykdGY4/678N+KmDYNQ1Fq2jX621QaJ6e31EMgByN+KeNpweo4K4qqppv/AFb6RF6pncDVGpwO/tYxUfggtWiIgIiICIiAiIgIiICIiAiIgIiICIiAqS7W7RX3/a1Pa7fG2Sqlp4WxsLg0OLYe0xk4A4K7Sqrav9ZekfXTt4tpTLnw7KmEH3lBXq7aQ1RZ3ubcLJWwBv03RO3D5PGWn3Fa0vVRdKa3W+oO9PRQSHvfG1x+IQeXC7NPSVVU/cp6eWV31WNLz9gyvTdllszDllspGkdRCwfgsixjGN3WNDQOgGAg87bXsv19dXNFPp2saD9Kdvq7cd+Zd3Kl/Tno5V8j2S3+6xxMzkwUvtvI7i9wAafIFW2RBrum9L2LTNCKK00TII+BeRxfI4fSe48SVsSIg0DWOzbSurm79wpCyqDcNq4cMmAHIE8Q4DuIKhV+yHaRpiR8mlNUl8OciAyOgJ82Hejd5nCtSiCqv57berF7Nx0366G8HP8AVTJ796lIaPNP9Ia/Ufs3HR264c/lXw/B7HK1SIKtf6TEOOOlH5//ADB/6a4/9IS/13s2vRpc48G/KyT8fJjGq0nYw5z2bM9+AuVBUC81O3HWFsrTVUTrZbWwSPnj3fVQ5jWklpDyZHAgcuR6rdfRukB0reY+rbmXf1omj8FYCspxU0dTTnlLE9h/eGPxVZ/RsqCyPVNC/g+OSnk3Tz477XfZgILRIiICIiAiIgIiICIiAiIgIiICIiAiIgKhOnKHXFbq/UtfpGYtq6apme9rXtaXxySn2cP9lwyORV8KidlPBNPIcMjjc9x8GjJVYPRuhfLLqyveOL30zAfEl7nfeEHE3bDtPsnyd90cX7vAydjLBveO97TT7guZnpLRDhLpR7XDmBWA/fGFaRcT4IZPnxMd5tB+9BV6T0lmHhDpRznHlms/ARlcf8NW0e58LPovO9yPYz1GPezdCtKyGGP5kbW+QA+5cqCqvqfpC6n9mWo/JdO/rvMpsZ/o96VbFp30f7VDUCt1Hc5rnOXbzomlzIyf13Elz/grEIg61JSUtFTRU1LBHDBE0NjijaGtaB0AHILsoiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgKqG1B35sbXtNaid7NPOIXSv/oz2Uo9zCERBaxrg4Ag5B4gjqv2iICIiAiIgIiICIiAiIgIiICIiAiIg69VVQUlLPVTvDIoY3SSPPJrWDJJ8gFV/YPDLeNWau1PKwjtS5oJ+tUydq4Dy3R9qIgtQiIgIiICIiAiIgIiICIiAiIgKp+ipBpPbhfbTMezhr3zMhzwHypFRF8PZHiURBbBERAREQEREBERAREQEREBERAREQEREEd7VL5HZdB32cv3ZJqd1NCORL5/Y4eIBJ9y1XYHZ30GhGVL24fX1cs4zz3G4jb7vZJHmiIJuREQEREBERAREQEREBERAREQEREBERAREQEREBERB//Z)"
      ],
      "metadata": {
        "id": "rBGq9T9efPVR"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# What is polars?\n",
        " \n",
        "* Polars is a library for working with and manipulating dataframe that is typically used for data loading, transformation and analysis.\n",
        "* It works conveniently with CSV files, Excel spreadsheets, json etc...\n",
        "* It is a faster alternative to pandas"
      ],
      "metadata": {
        "id": "fssVmHOb-l4v"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Why polars vs pandas?\n",
        "\n",
        "* Polars is much faster.\n",
        "* Polars implements under-the-hood code optimization, including native parallelization.\n",
        "* Polars code is easy and pandas-like."
      ],
      "metadata": {
        "id": "hEm_mFRK-xls"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Import both libraries\n",
        "\n",
        "import polars as pl\n",
        "import pandas as pd"
      ],
      "metadata": {
        "id": "JRVyu6xi_soj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Sample dataset ~ 14000 rows and 20 columns\n",
        "\n",
        "csv_file = 'RankingsCombined.csv'\n",
        "pl.scan_csv(csv_file, ignore_errors=True).head(5).collect()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 362
        },
        "id": "56XJmt9B_srC",
        "outputId": "f598f867-d7a0-45ec-e8d9-d68ca8bfa822"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "shape: (5, 25)\n",
              "┌─────┬────────────┬──────┬──────────────┬───┬────────────┬────────────┬────────────┬──────────────┐\n",
              "│     ┆ rank_order ┆ rank ┆ name         ┆ … ┆ stats_numb ┆ stats_stud ┆ stats_pc_i ┆ stats_female │\n",
              "│ --- ┆ ---        ┆ ---  ┆ ---          ┆   ┆ er_student ┆ ent_staff_ ┆ ntl_studen ┆ _male_ratio  │\n",
              "│ i64 ┆ i64        ┆ i64  ┆ str          ┆   ┆ s          ┆ ratio      ┆ ts         ┆ ---          │\n",
              "│     ┆            ┆      ┆              ┆   ┆ ---        ┆ ---        ┆ ---        ┆ str          │\n",
              "│     ┆            ┆      ┆              ┆   ┆ str        ┆ str        ┆ str        ┆              │\n",
              "╞═════╪════════════╪══════╪══════════════╪═══╪════════════╪════════════╪════════════╪══════════════╡\n",
              "│ 0   ┆ 1          ┆ 1    ┆ Harvard      ┆ … ┆ null       ┆ null       ┆ null       ┆ null         │\n",
              "│     ┆            ┆      ┆ University   ┆   ┆            ┆            ┆            ┆              │\n",
              "│ 1   ┆ 2          ┆ 2    ┆ California   ┆ … ┆ null       ┆ null       ┆ null       ┆ null         │\n",
              "│     ┆            ┆      ┆ Institute of ┆   ┆            ┆            ┆            ┆              │\n",
              "│     ┆            ┆      ┆ Technolo…    ┆   ┆            ┆            ┆            ┆              │\n",
              "│ 2   ┆ 3          ┆ 3    ┆ Massachusett ┆ … ┆ null       ┆ null       ┆ null       ┆ null         │\n",
              "│     ┆            ┆      ┆ s Institute  ┆   ┆            ┆            ┆            ┆              │\n",
              "│     ┆            ┆      ┆ of Techn…    ┆   ┆            ┆            ┆            ┆              │\n",
              "│ 3   ┆ 4          ┆ 4    ┆ Stanford     ┆ … ┆ null       ┆ null       ┆ null       ┆ null         │\n",
              "│     ┆            ┆      ┆ University   ┆   ┆            ┆            ┆            ┆              │\n",
              "│ 4   ┆ 5          ┆ 5    ┆ Princeton    ┆ … ┆ null       ┆ null       ┆ null       ┆ null         │\n",
              "│     ┆            ┆      ┆ University   ┆   ┆            ┆            ┆            ┆              │\n",
              "└─────┴────────────┴──────┴──────────────┴───┴────────────┴────────────┴────────────┴──────────────┘"
            ],
            "text/html": [
              "<div><style>\n",
              ".dataframe > thead > tr > th,\n",
              ".dataframe > tbody > tr > td {\n",
              "  text-align: right;\n",
              "}\n",
              "</style>\n",
              "<small>shape: (5, 25)</small><table border=\"1\" class=\"dataframe\"><thead><tr><th></th><th>rank_order</th><th>rank</th><th>name</th><th>scores_overall</th><th>scores_overall_rank</th><th>scores_teaching</th><th>scores_teaching_rank</th><th>scores_international_outlook</th><th>scores_international_outlook_rank</th><th>scores_industry_income</th><th>scores_industry_income_rank</th><th>scores_research</th><th>scores_research_rank</th><th>scores_citations</th><th>scores_citations_rank</th><th>location</th><th>aliases</th><th>subjects_offered</th><th>closed</th><th>unaccredited</th><th>stats_number_students</th><th>stats_student_staff_ratio</th><th>stats_pc_intl_students</th><th>stats_female_male_ratio</th></tr><tr><td>i64</td><td>i64</td><td>i64</td><td>str</td><td>f64</td><td>i64</td><td>f64</td><td>i64</td><td>str</td><td>i64</td><td>str</td><td>i64</td><td>f64</td><td>i64</td><td>f64</td><td>i64</td><td>str</td><td>str</td><td>str</td><td>bool</td><td>bool</td><td>str</td><td>str</td><td>str</td><td>str</td></tr></thead><tbody><tr><td>0</td><td>1</td><td>1</td><td>&quot;Harvard Univer…</td><td>96.1</td><td>1</td><td>99.7</td><td>1</td><td>&quot;72.4&quot;</td><td>49</td><td>&quot;34.5&quot;</td><td>105</td><td>98.7</td><td>2</td><td>98.8</td><td>8</td><td>&quot;United States&quot;</td><td>&quot;Harvard Univer…</td><td>&quot;Mathematics &amp; …</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>1</td><td>2</td><td>2</td><td>&quot;California Ins…</td><td>96.0</td><td>2</td><td>97.7</td><td>4</td><td>&quot;54.6&quot;</td><td>93</td><td>&quot;83.7&quot;</td><td>24</td><td>98.0</td><td>4</td><td>99.9</td><td>1</td><td>&quot;United States&quot;</td><td>&quot;California Ins…</td><td>&quot;Languages, Lit…</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>2</td><td>3</td><td>3</td><td>&quot;Massachusetts …</td><td>95.6</td><td>3</td><td>97.8</td><td>3</td><td>&quot;82.3&quot;</td><td>36</td><td>&quot;87.5&quot;</td><td>21</td><td>91.4</td><td>11</td><td>99.9</td><td>2</td><td>&quot;United States&quot;</td><td>&quot;Massachusetts …</td><td>&quot;Mathematics &amp; …</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>3</td><td>4</td><td>4</td><td>&quot;Stanford Unive…</td><td>94.3</td><td>4</td><td>98.3</td><td>2</td><td>&quot;29.5&quot;</td><td>156</td><td>&quot;64.3&quot;</td><td>33</td><td>98.1</td><td>3</td><td>99.2</td><td>6</td><td>&quot;United States&quot;</td><td>&quot;Stanford Unive…</td><td>&quot;Physics &amp; Astr…</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>4</td><td>5</td><td>5</td><td>&quot;Princeton Univ…</td><td>94.2</td><td>5</td><td>90.9</td><td>6</td><td>&quot;70.3&quot;</td><td>53</td><td>&quot;-&quot;</td><td>164</td><td>95.4</td><td>5</td><td>99.9</td><td>3</td><td>&quot;United States&quot;</td><td>&quot;Princeton Univ…</td><td>&quot;Languages, Lit…</td><td>false</td><td>false</td><td>null</td><td>null</td><td>null</td><td>null</td></tr></tbody></table></div>"
            ]
          },
          "metadata": {},
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Polars data read performance\n",
        "\n",
        "%%timeit -n1 -r1\n",
        "pl.read_csv(csv_file, ignore_errors=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OWK748wC_stb",
        "outputId": "836694ae-f78e-4d84-8b52-90afd3eb5614"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "60.8 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Pandas data read performance\n",
        "\n",
        "%%timeit -n1 -r1\n",
        "pd.read_csv(csv_file)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "547jvSrs_sv0",
        "outputId": "de52f645-308a-438a-8134-ee9d6146c3d7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "158 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Optimized pandas data read performance\n",
        "\n",
        "%%timeit -n1 -r1\n",
        "pd.read_csv(csv_file, engine = 'pyarrow')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w4VbWNBgDiQF",
        "outputId": "ddd16d22-8022-461b-e91d-79bd411c27a0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "114 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Query optimization\n",
        "\n",
        "By default, polars also optimizes queries, which makes them easier to read and write. \n",
        "\n",
        "For example, here is a comparinsong of getting an average and maximum values grouping by the location."
      ],
      "metadata": {
        "id": "wm_Qks1uE51C"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Polars aggregation\n",
        "\n",
        "%%timeit -n1 -r1\n",
        "(\n",
        "    pl.scan_csv(csv_file, ignore_errors = True)\n",
        "    .groupby('location')\n",
        "    .agg(\n",
        "        [\n",
        "            pl.col('scores_industry_income_rank').mean().suffix('_mean'),\n",
        "            pl.col('scores_industry_income_rank').mean().suffix('_max')\n",
        "        ]\n",
        "    )\n",
        "    .collect()\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MdZ09htfE9M4",
        "outputId": "45840eb8-5b68-41c8-bc71-982419a0b9a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "28 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        " # Pandas aggregation\n",
        "\n",
        "%%timeit -n1 -r1\n",
        "(\n",
        "    pd.read_csv(csv_file)\n",
        "    .groupby('location')\n",
        "    .agg({'scores_industry_income_rank': ['mean', 'max']})\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9jfRo1v_IPZq",
        "outputId": "a793de88-8ab9-4609-f966-c97561d39145"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "150 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Polars vs pandas aggregation\n",
        "\n",
        "%%timeit -n1 -r1\n",
        "(\n",
        "    pd.read_csv(csv_file, engine = 'pyarrow', usecols = ['location', 'scores_industry_income_rank'])\n",
        "    .groupby('location')\n",
        "    .agg({'scores_industry_income_rank':['mean', 'max']})\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JhlaaflOIPcT",
        "outputId": "705123f7-abf9-488d-ba34-7153725a2097"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "41.7 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Conclusion\n",
        "\n",
        "Even on a relatively small dataset polars is about 3 times faster than pandas and about 2 times faster than using pandas with optimization."
      ],
      "metadata": {
        "id": "mloFuUKYIPel"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "2MEtiE8mIPhN"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}