# Pedra, Papel e Tesoura – Python

Projeto simples em Python que implementa o clássico jogo **Pedra, Papel e Tesoura**, permitindo que o usuário jogue contra o computador pelo terminal.

## Como funciona

- O usuário escolhe entre **Pedra**, **Papel** ou **Tesoura**
- O computador faz uma escolha aleatória
- O vencedor da rodada é definido com base nas regras do jogo
- Ao final de cada rodada, o usuário pode escolher se deseja jogar novamente

## Lógica utilizada

A lógica do jogo é baseada em um **dicionário**, onde cada chave representa uma jogada e seu valor representa qual jogada ela vence.  
Isso evita o uso excessivo de condicionais (`if/elif`) e deixa o código mais limpo e legível.

Exemplo:
```python
jogo = {
    'Pedra': 'Tesoura',
    'Papel': 'Pedra',
    'Tesoura': 'Papel'
}
