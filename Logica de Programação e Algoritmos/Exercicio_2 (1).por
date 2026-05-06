programa {
  funcao inicio() {
    real raio, altura, area, volume, pi=3.14
    
    escreva("raio:")
    leia(raio)
    escreva("altura:")
    leia(altura)

    volume=(2*pi*raio*(raio*altura))
    area=(pi*raio*raio*altura)

    escreva("\n volume:",volume)
    escreva("\n area:", area)

  }
}
