# Sign-Language-Classification

## Deploy to Azure

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fjanczarek99%2Fsign-language-classification%2Fmain%2Fazure-deploy-template.json)

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

![architektura](resources/architecture.svg)
