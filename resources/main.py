from flask import Blueprint, render_template

main_resource = Blueprint('main', __name__, url_prefix='/knock/main')


class TmpImage():
    hashed_name = "jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEBUQExMVFRUXGBUXGBcXFhgVFRcVFRUXFxUVFxUYHSggGB4lGxYVITEhJSkrMC4uFx8zODUsNygtLisBCgoKDg0OGxAQGy0lICYwLS01Mi0tLS8tKy0tLS0uLS0uLS4tKy0tLTIuLS0tLi0tLSstLSstLS0vLS4tKzUuLf/AABEIAMIBAwMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABAMFBgcIAgH/xABFEAACAQICBwYDBgMFBgcAAAABAgADEQQhBQYSMUFRYQcTInGBkTJSsRRCcoKhwWLR8BUjkqLCM0Oy0uHxJDRFVGNzk//EABoBAQADAQEBAAAAAAAAAAAAAAABAgMEBQb/xAAwEQEAAgIAAwQIBgMAAAAAAAAAAQIDEQQhMRITUWEFIjJBgZGh0RVCcbHB4RQz8P/aAAwDAQACEQMRAD8A3jERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERARI+NxtOim3VqLTW4W7MFG0xsq3PEnICVKFZXUOjBlO4g3B9YFSIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiWjS2s2DwwPfYmkhH3doF/RBdj7TBdY+0hnwlWvhR3VPNKdRx46j3szInBRfLiTfdsm8b9y0UtreuTM9ZNcMHgR/4isA9rimviqH8o3DqbCY3o/tBxGNYjAYPbA3vVqAAearkP8AFObtK41nqs5JJYgkklmJsAWLEkkm1z55WE292H6S7vA4i2b98thz2wqJfptbV+l5aIUmWwWq6XbfUwdL8KVHI9S1pb69PSTf+qIOiUaf/KTJdSpc+IlzzO70XcPT9Z5er1l+zCNyxfWLVjF4ymKWIxxrIGDhWQoA4BUHwoODN7yM+jNK0VtTxdSw4I6jcAL2NrmwGe8zLDWgVpGjm1hpDWfSNE7L4zFKet/5Zy3t2iY5d2Pr+qqfqs2xjcOlVSrKGHUXmtdc9TdkGrh1uN5TjbmvPyldJRKfanpFd2NY/ioof9EuOE7atIIfE1CoP4qTKfdSJq7EnO3nf+U+UBc2uZCW99Fdu6mwxGE/NRqhv8jhfrNh6s684HH+GhWHeb+6cGnU9Fb4vMXnItRSMjKuCxJRgwJUgggjgRuPQ9YHbETRuona5Up7NHHXqU9wrDN1/H8467/ObsweKSqi1abB0YXVlNwRArREQEREBERAREQEREBERAREQEwrtQ10/s3DqKVjiKpIQHMKo+KoRxtkAOZ6TNZz/wBrNWhisXUKVy1aiQrU9k7KUyuRBtmL5tyL+ci29cmmKK9uO10W7Q2sDVvtFfF4/GI6UzURqTmxYMF2Su0AM2WwFhvzHHHMfrxi6w7tsVV2P/kq1H9Sq5HyIMp6HA700KpCrVU0yx+EFrGmxPy7aoSeV40djMNhmK1MHQrMpN2qGs3HhsVAlvQzGvKOb08/r2iKdmI15fSX3SOr9eiwDVqFZjs3SjU22TaNl21sAhJIFt+cu3aNX7l0wa/7OgopqBuZk8JYjmW7w/nMvGjNbNEO4NbBLQfaDd7SNT4gdoMwvnnnYhhLDrFiKWJrvUuDtEsrbJK+Jma9viW5Y26WmlZjblzUydjW+1+k7/bbBWJJuZszsirW204XVj+Van7lZgmK0eVJbIqOKkG/K9sx6zNezuuqVqtyBdFRepAGQ9BNI6uGejZiYmSErSzox5GSKTnkZorCezSkWnkPPLGEvfeT6xDCxlAtPgeVka37Q9U7XxVFerqOI+cdec17TpMxAUFidwAufYTomqm0LEXmu9OarGg96LFEqFi2yuYGVl29q9jn4QLbt+4V0nbEho17DvkZTzFiw5Ns7z1EiYnAMnIqdzjMHp0PSZbS0aijNbjqAQOfhE8YhKSAtuQ5NkWW38Qt5b40mLR0li+GZlyO7nymb6ia9VtG1LZ1MOx8dK+7+OnyPTjMarUaOTBiqt8JHiTyF8/S5npNHG11dGXmMh+8IdXaF0vRxdBcRQcOjbiN4PFWHAjlJdaqqKWYhVAuSTYADiTOY9Utbqmiq3eK6tSYgVaIa+2vzAcGHAzcOvGs7PooYzR9QVGBpVNlbM+w2RJp5m6llbdls34SJWrG5ZDQ1xwDv3a4ujtXtYuFN+XitL7OUsbpuvjmRKqLWqk+F6du+I3bBAyYXtYkZes6N1MAoYDD0KlQd4tNQwaorMpOewSDns32fSVrNp6w2z0xV13dtsgiIlmBERAREQEREBERATlnV+g5x74sFSWr10sxOe1tBb9NtkG+dTTlKhiLO2HUEOr4kk77kk2sOAUKTAyPSWraYja2Kb0aoBYra9MHmrDnfct/Ib5g2k9GPSfZqqVPPgR0O4zI6mmcbUTumfZBIu6+F8jfepH0lRcS5Xu67Cun8eTjqtTf73lJrvo6qZorytqYYTWw9hcMcuBlzwOK2qa3sTa3wrwJsN3K0mY/QtgalEmom8r/ALxRxuOI6jKWrRKAGzk7AuzkC5CjeByJ3eZmdomY1LswXx48veU6a5r1gsH3zKi0zVZjZaajaZiPTIf1lvmdaD7J8S3irLTogttW75hUU8PhDLu4Xmtl0/3zin3a00F1plRZlvuDsANq/PrL1oTW7F4ZvBWcAGxRiXTLhsnd6Wldd23i9eMidaifOP5bexeq9TDqCWxFReJpd3UK+alNtvQEyHo+jQqsQMa6kb1NJC457a22kz5qP5V9U9f1xICP4Kvy38LdUP7fWXvSmAw+LsaqAuPhqL4aq/hcZ+huOk1jJvnWXJbg4p6uSuvOPt/angNXi63GNSstrArRpAgg5EtT38cv1lYatsBnVQnpTK/6jML03onHYQNUw9Tv0IsSV/v04Bgy2YnPeCc+A3S2aI7SMZROxX2awGR2/BUFuG0B9QZH+RFeVmlPRNskdrHMT+7YGI1eqAXRqbHkSy/rYzDNO4/GYa+3gyq/PtF6fntJkPUiZXojXvB4iw7zunP3allz6P8ACfe/SZB30tN+1HqyzrwsYbay49/ruP8Avq0hW1uxR+EUlH4WP6l5CxencRVXZfu2B/hcfqribe0tqxg8RcvRVWP36fga/M2yPqJh+leziot2w9UVB8r+Fv8AEMj7CYWtmj37ejh4f0df2qzWfOZ/ff2YRhdKYimpVXWxJtdWYrfgpZibdDeUHxdU72W3LYFs+GeY95O0hourQNqtNk6kZHyYZH3kMrMf8jJ4u+PRHCTG4rv4z91veg531aluQYiRX0SpJJLEnfc3v5y7lZ5Kx39/FP4Vw0fk/f7rR/ZFPr7yVRqtTsAbgCwBzsBusd49JKKylVp3EnvbT1lE+j8NfZrD5h6gLHwICflGz6XvJCoh+4v0P6SBTaxvL/p7BKgoV6Z8FalTPlURQlW/m6ufeVtuV8UY6REa6q+i9P4vC+LD4ioAMyjHbW3VGuCOot6TZGqHaulZ1oYxVoubAVVP90x6g5p7keU08lcjPjPOKQMNoDLcRyP8jw9RLUy2qx4v0fgyxyjU+Mfy6wBiaf7I9ezddHYlr8KFQnP/AOpj9D6TcE7a2i0bh8rmw2xXmliIiWZEREBERATmHXCmMPja3d2pt31emxvmyvVa4F8hdeVjmRnOnpz7rjotX03imJG1Tp16yLbeyUhULEnkGuBzEmBgT6SdgNkhfr7yhiq7OfFw4fvPOFXwKegnuou4ykt40+4Z3QhkYqRusZX0rpQtQde7VWcrtuosWCm9iNwz5b7Smko6RW9M+n1EImVXA6GZ6V1DXsTuGzkpYgtfIkDLLlzy9VELKHHxceRIyJnvEBqDV1BOasoN8ie8prkPw39J9o1hc3y2tlh+db2k2jcGDJNL7gwuKK+IX8Piy3jZzuOOW/0mw9Vu0WiyinXqhWG52uobzysDNdsCjCom8G/P9DkfLjL9gtUauNR8RgaVJkLbTUjVVHo1PvIu1vQ5FbncBymFMUbern428Y4mIiY8+sNxaN0/QrDwVab/AIXVv0BkolEO06I6fMyhmp+ZIvs9eHlmNCYrUjSiEE4J7c27qqg5ePML7y5UhpDDZ9zjEy3Ia6gHlcl6X+Wa9jTjjiotz7M/BvPF4PD1hapRpOOqKfY2kKhoGlS/8vUq0R8qttU//wA6m0B6WM1Fgu0SrR8BqtTy+DEUBUUHiA9IowHTYysbZWAyjRvaQhANcJsmw7yg5qKCd23ScLUT2Miae/TXHxET6sWmPKen2bBFJ7WJVuq+H/KSfrI9WqyHpIuG0sjqHQllIuCoLAjoVuJVOkFtYkfmFvrKbdUUmOqs1VKi2YBgd4Iv7gzF9Mak0Kl2pf3Tchmn+Hh6Wl5LUybqwB6EEe0qCqf+0ztET1dGK18c7pOmqdLaDrYc/wB4vh+dc19+HrLWVm5qxDAhhcHpeYNrLq+i3qUvDzUghfym2XlunPfHrnD1cHGRf1bxqWHkSmwlcymwmcS6rVQK62N+cnVq7FEp/dVQQLcWHiN+OcplcweRB9jeK9S7E2A3AAbgBumsW5OG2Oe35dVMz5SextYkHIgbyOnUbx1E+MZHr09oFb24+gIJk1jc81c95ikzWNylYOjets7TKVKsSBbZGRvfnbO2U6a1X0l31GzMGqU7KzfMLeGp+YfqG5Tl/C12pWKGxB2r7yWHE33+W6bc7MtNd5jURSQHpeJTuuNprKSSzEG13YksSx8INp247U1qr5ni8OeJ7eWev0bdiImjgIiICIiAmgO2nDtR0lUxCuq7VDdezMKyGgwUcRZDcjdlfeJv+a47YNRqmkkpPRKipS2gL38Sta63HUA+/OBztgsSNnYORF7db5yRh2LX5DieJ4gSTpXUfG4e+3SyHFcxLRh8TUotYjcfhbd/0hPaldSLQRfLqPrJuAppig3dsi1AL92fCWsMwp3X6ZXkGmhD2OViLg+Yy/WV6NYmLQqaTBKlrg22FbmrKq5+o/fkZGsSoHOncflbL9AZXooVqszZhzdxyG1dR55+wMqYyilKvTWm20pW4PHPbyPlaWZRy5oWFrH4b+UyDVjWWtgKxrUSPENl1N9lhwuARmDmD585jBGy3kfoZPEzdv8ALZ9HtZqMjCthKNVSLMEqsGIbI3p1FfK2/eM98tmje1VKbmm1Kr3P3butSrT/AICRbbUcCbEAZ3mB1F6C3OVPspfjtefi9tq9pW+aOlm+DgsntYvk2/hu0DR9cWNdPw1VK/8AGLfrK/8AZ2jcR4hQwtTjtIqfVN80tidX3XNqLKOeywHvmP0lvOjypuCwPTP+Urus9Jbz3tfax7/Ru0aA+zOamCcoCbtQck0m/Cd6HrnL3h8WSBcFTxBsbHzGRmhMPpfFUvhxNZehZiPY5S4Udeccm+sr/iRT+tgZHYn3LxxdNamJhvEsDPDUl+VfYTUWH7TcSPipUm8tpT9TLnQ7Vfnwx/LU/YrHZlpHE4vFsY01+Ue0pVaKEfCPYTDaXahhT8VKsvorf6pIHaDgT99x502/a8rNZX77HP5oR9ZtDBb1UA6i2XmBLXpPR9JKaVKVQOGAJUlNtbgb1XMWbaU36HjLritesCQRtsfJG/eYXitM0NolNrZvldc5z5MVt8oduHi6TrtZIjX6c48EoyhVkN9NU+Ab2ketpgHcp9TFcV/Bpl4/h4j2kxjKNRgMybfpLZV0mx5CUPtfHMmdFcE+95Ob0pTpSPmuJxJY7NMXPzH4R5DjNidkdQU9JUAzXYhkJ4502A/UCauTSLAWVQOuZPvMg7OMXWOlsGFO+vTuLDNQ12/y3m9a66PLy8RGTc2mZn6OtIiJo4iIiAiIgIiIEXE4BKgsyg+kwTWrszw9cFlUK3SbFnwiByfrLqRXwb7Sg2BuCN49ZEGnlr0+6xQAqqBsVwPF4cwlS28dc7TqrSmhqddSrqCDNGdo/ZY9HaxGH8S7yvEQMKxDd7ie7T4RtEnfcohYk8sxYeUtdSuSyMcju9iRMh1dwbGp9psSoQo2WSsV2TtcrsCJjekHAqnkDb0vJHpzc36yYHFpBZ7588/SeQLm17czy/mZi7+WlbE422S5nnwEgtUqHex9/wBpOp4cblIP6Gejhzfd/VxLR2WNozT0ifh/S2gvzPuY2n5t7mXDuenLh5/1afO66f1YS3qs9ZY90/Vbyzcz7mfCx6y4d1/XqZ4NLL+uQ/q0clfX80HaMbZk00fr+8pmj/XpHI9bzUATPO3K4SxuJVrYXa+HfylZmI6tq0vaPVQ+8jvJ77gz6MOZO6qxTLKncwFJkunhzY+U+pS6SIvC1uHyctQjrRlQUZLWgZVWhInLWGlOAy28kMUpe9TdKfYsdQxextCm1yvNWUo1uuyxI6gSGqjdvPIZn2En6PwgZ1Dg2JFwpAci+YUZ523X9jI7drdIXnhsOP8A2X+EOs6NUModcwwBHkRcT3I2jSO5p7Kso2EsrCzKNkWVhwI3GSZq88iIgIiICIiAiIgJTq0gwswuDKkQOdO1jRraOxztTQdxiB3lM5gU61tmsoIO82DWOXiFt01a9TO+/wA+PnOwtZdWMPjqfd112hv9eBmp9P8AYkoJbDuwHIm8DTX2gHIlh67Q/XMSRh+7tY2PUNY/4TaZJpLs3xNIkWJmP4vQFWnvU+0HR7+yKdxYeYv9Jc9G6cxGHBphErJyqJcjyO/3vMaOGccCJ8JccW9zImsS1rmyV6SzOnrMfv6OpN+Fdn9p9Om8M3xaNcfhdvpYTCjUf5m9zPBduZ9zKd1Xwbxx+ePzM1fSGBO/C4tfwlT/AMUptiNH/LjF80pn9xMMM+R3VVo9I5/GGXtU0cd1esv4qAP0eeSuA/8Adt64d/2JmJRI7mqfxLL4R8mVmlguGLHrRq/yhBhFIIxa3Bv/ALKtw/LMUiO5qfiOXwj5MrxtXBM5cVgt8yqUn2b8bbRFgTwltfF0Qcix/Lb95ZojuYI9IZPCPku39o0xuVv0lNtJjgnuf+kts9BTJjFVW3pDPPv18ISn0i53WHkP5yi2JY7yT9PafFoE8JJoaOduBlorEdIc982S/tWmWUalaVoIwFeijjqLj2OU35qnpfCMoFJUp9FVV+gnPmiNX6pIsp9ptbU/VmtldSB1lmTbiNcXE9SLo/DGmgUm8lQEREBERAREQEREBERAT4RPsQKFbCq29QZacdqxh6ozQe0vsQNeaQ7M6DZqLTHcZ2Ug/CJuS0WgaDxHZPUG4S31uy2v8s6MtPmwIHNVTswxHySJV7NcQPuGdPmmOU8miOQgctN2eYgfcPtKZ1BxHyH2nVH2ZflE+fZE+UQOVW1ExHyH2npNQMSf92fadTnBp8o9oGET5R7QOZKPZpiT9wyXS7Lq5+6Z0mKI5Ceu7HIQOe8N2S1TvEvWD7I+c3WFn20DV+D7KKQ+KZDgdQMLT+4DMvtPsC24XQtGn8NNR6SelMDcLT3EBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQERED//Z"


class TmpLecture():
    idx = 1
    title = "안녕"
    description = "안녕하세요"
    image = TmpImage()


@main_resource.route('/')
def main_page():
    image_path = "data:image/"
    a = []
    a.append(TmpLecture())
    a.append(TmpLecture())
    a.append(TmpLecture())
    a.append(TmpLecture())
    a.append(TmpLecture())
    a.append(TmpLecture())
    a.append(TmpLecture())
    a.append(TmpLecture())
    a.append(TmpLecture())
    return render_template(
        'main.html', image_path=image_path, lectures=a)
