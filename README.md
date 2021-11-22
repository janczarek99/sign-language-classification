# Sign-Language-Classification

## Cel projektu

Celem projektu było stworzenie serwisu do rozpoznawania alfabetu migowego na podstawie przesłanego zdjęcia (możliwe formaty: .jpg, .png, .bmp).

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

## Demo rozwiązania

[![demo](resources/images/thumbnail.png)](https://www.youtube.com/watch?v=aSBm_2dLl_I)

## Reprodukcja rozwiązania

Poniżej znajdują się dwa przyciski, które służą do szybkiego wdrożenia serwisów użytych do stworzenia naszej aplikacji przy użyciu szablonów ARM (Azure Resource Manager).

### Custom Vision

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fjanczarek99%2Fsign-language-classification%2Fmain%2Fresources%2Fazure-deploy-templates%2Fcustom-vision-template.json)

### Container Services

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fjanczarek99%2Fsign-language-classification%2Fmain%2Fresources%2Fazure-deploy-templates%2Fcontainers-template.json)
