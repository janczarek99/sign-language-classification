# Sign-Language-Classification

## Wdróż na platformie Azure

### Custom Vision

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fjanczarek99%2Fsign-language-classification%2Fmain%2Fresources%2Fazure-deploy-templates%2Fcustom-vision-template.json)

### Container Services

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fjanczarek99%2Fsign-language-classification%2Fmain%2Fresources%2Fazure-deploy-templates%2Fcontainers-template.json)

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
