# Polish-Sign-Language-Classification

## Cel projektu

Celem projektu było stworzenie serwisu do rozpoznawania polskiego alfabetu migowego na podstawie przesłanego zdjęcia (możliwe formaty: .jpg, .png, .bmp).

## Skład zespołu

* Damian Jaczarek - [github](https://github.com/janczarek99)
* Hubert Piłka - [github](https://github.com/MrBallOG)

## Stos technologiczny

* Python (Flask)
* Docker
* Azure Custom Vision
* Azure Container Services:
  * Container Instances
  * Container Registry

## Diagram architektury

![architektura](resources/architecture/architecture.svg)

## Sposób działania

Główną częścią aplikacji jest serwis Custom Vision, który przetwarza obrazy przy pomocy klasyfikacji wieloklasowej, która pozwala przypisać jednemu obrazowi dokładnie jedną klasę. W celu wyuczenia modelu do rozpoznawania polskiego języka migowego stworzony został specjalny zbiór danych, którego przeważająca większość obrazów pochodzi ze zbioru udostępnionego na stonie [dataverse.harvard.edu](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/K142HP), a także własnych przeszukiwań internetu. Zdjęcia zostały załadowane do serwisu Custom Vision, a następnie otagowane.

![obrazy treningowe](resources/images/training-images.png)

Jak się okazało statyczna interpretacja znaków polskiego języka migowego jest właściwie niewykonalna, gdyż różnice między znakami diakrytycznymi, a ich odpowiednikami wynikają z ruchu ręki. W związku z tym model został uproszczony do rozpoznawania podstawowych znaków (a, b, c..., z). Następnie model został wytrenowany.

![wydajność](resources/images/performance.png)

Otrzymany w wyniku model został opublikowany w formie API, dostępnego za podaniem klucza. W celu umożliwienia interakcji z modelem powstała aplikacja webowa we Flask'u, która w formie kontenera została dodana do serwisu Container Registry i tam zbudowana. Następnie przy pomocy serwisu Container Instances aplikacja została wdrożona. Interfejs użytkownika jest bardzo prosty, wystarczy dodać lokalny plik (klikając "Przeglądaj..."), a następnie nacisnąć przycisk "classify". Następnie po prawej stronie ekranu wyświetli się przesłany obraz, a pod nim informacja o wykrytym znaku.

![strona](resources/images/website.png)

Link do strony - <http://classify-sign.westeurope.azurecontainer.io/>

## Demo rozwiązania

[![demo](resources/images/thumbnail.png)](https://www.youtube.com/watch?v=aSBm_2dLl_I)

## Reprodukcja rozwiązania

Poniżej znajdują się dwa przyciski, które służą do szybkiego wdrożenia serwisów użytych do stworzenia naszej aplikacji przy użyciu szablonów ARM (Azure Resource Manager).

### Custom Vision

[![wdróż na azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fjanczarek99%2Fsign-language-classification%2Fmain%2Fresources%2Fazure-deploy-templates%2Fcustom-vision-template.json)

### Container Services

[![wdróż na azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fjanczarek99%2Fsign-language-classification%2Fmain%2Fresources%2Fazure-deploy-templates%2Fcontainers-template.json)
