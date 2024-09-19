# Data Engineer Challenge - Solução

## Descrição

O projeto tem como objetivo desenvolver um pipeline de dados que captura dados da PokeApi, insere-os em uma tópico Kafka que será consumido a fim de fazer uma contagem dos tipos de Pokémons ingeridos

## Componentes do Sistema

1. **poke-api-producer**: Obtém dados dos Pokémons e envia para um tópico Kafka;
2. **poke-api-consumer**: Consome de um tópico Kafka, processa os dados e salva em um arquivo json (`type-counts.json`)

## Desenho da Arquitetura


<img src="arquitetura" width="1200" height="1000">

## Estrutura do Projeto

1. **poke-api-producer**:
   1. `application/`
      - `controller.py` - Orquestra a obtenção e envio de dados para o kafka 
   2. `entities/`
      - `pokemon.py` - Implementação da Classe Pokemon e seu modelo de dados
   3. `infrastrucutre/`
      - `messaging/kafka_producer.py` - Lida com a produção/envio de mensagens para o kafka
      - `poke_api/poke_api_client.py` - Cliente para interação com a PokeApi
   4. `test/` 
      - `controller_test.py` - Testes unitários da classe Controller, utiliza mocks do PokeApiClient e KafkaProducer para validar obtenção de dados e envio ao kafka
      - `mock_poke_api_client.py` - Simula o comportamento do PokeApiClient retornando dados simulados do `api_return_value.json`
      - `mock_kafka_producer.py` - Simula o comportamento do KafkaProducer ao enviar mensagens pro Kafka
      - `api_return_value.json` - Dados simulados de uma resposta da PokeApi

2. **poke-api-consumer**:
   1. `application/`
      - `controller.py` - Orquestra o consumo de dados do kafka, processamento e escrita no JSON.
   2. `entities/`
      - `pokemon.py` - Implementação da Classe Pokemon e seu modelo de dados
   3. `infrastrucutre/`
      - `messaging/kafka_consumer.py` - Lida com o consumo de mensagens do kafka
      - `file_handling/poke_api_client.py` - Gerencia operações com arquivos 
   4. `test/` 
      - `controller_test.py` - Testes unitários da classe Controller, utiliza mocks do FileHandler e KafkaConsumer para validar consumo de mensagens, processamento e escrita em arquivo
      - `mock_file_nandling.py` - Simula possíveis comportamentos do FileHandler ao lidar com arquivos
      - `mock_kafka_consumer.py` - Simula o comportamento do KafkaConsumer ao consumir mensagens do Kafka


## Diagramas de Sequência

### poke-api-producer

[![](https://mermaid.ink/img/pako:eNqFVMFu2zAM_RVBJwdLUPTqQ4G064Y06Gq0OxowNIlxhFiUJskYgiD_PjnyksiOO19sUu898hkUD5RrATSnDn63gBy-SlZbpkok4THMesmlYeiJYhIJc-Q1vMenTxq91U0DtsNcojGy0DtYGvnUSAhRACeJMX7NNjtWWC1aHsWTxIR-sTorF6sJzUcbji-KJMZlb66zu3h4-HKxkhOJzge6ZB4i6HLYQRMj_0UnNhJ05rWRvEKmYBaZCTaQr_rPCdeIwH22Xn5bL6vH97f18_tNXiAuru1Y8K3t7Sa9TyIjttHakA14viV8z5ve3chhItBiZUIJpbE6McFmswne4DfW4M_UX_tKiqzLWIZCqy6aXemkLnqpYtUZCNPtfPb9-Se569XuDlIch-RitRi3YMEZjQ6yl4-3H5PlhpZP_ywrYrEps4MpcICiUuAcq-EG9dM5MDF_NT1z0ksNJSJlMa7P-A71nwZErc6X8eYgTc3Rp1PgGgCT3RMlsfX_mgqOS6RzqsCGOyfCKjp0ByX1W1BQ0jx8CmZ3JS3xGHCs9fpjj5zm3rYwp1a39ZbmG9a4ELVGhBvUL7FzFoT02r7GTXdaeMe_MXKyaw?type=png)](https://mermaid.live/edit#pako:eNqFVMFu2zAM_RVBJwdLUPTqQ4G064Y06Gq0OxowNIlxhFiUJskYgiD_PjnyksiOO19sUu898hkUD5RrATSnDn63gBy-SlZbpkok4THMesmlYeiJYhIJc-Q1vMenTxq91U0DtsNcojGy0DtYGvnUSAhRACeJMX7NNjtWWC1aHsWTxIR-sTorF6sJzUcbji-KJMZlb66zu3h4-HKxkhOJzge6ZB4i6HLYQRMj_0UnNhJ05rWRvEKmYBaZCTaQr_rPCdeIwH22Xn5bL6vH97f18_tNXiAuru1Y8K3t7Sa9TyIjttHakA14viV8z5ve3chhItBiZUIJpbE6McFmswne4DfW4M_UX_tKiqzLWIZCqy6aXemkLnqpYtUZCNPtfPb9-Se569XuDlIch-RitRi3YMEZjQ6yl4-3H5PlhpZP_ywrYrEps4MpcICiUuAcq-EG9dM5MDF_NT1z0ksNJSJlMa7P-A71nwZErc6X8eYgTc3Rp1PgGgCT3RMlsfX_mgqOS6RzqsCGOyfCKjp0ByX1W1BQ0jx8CmZ3JS3xGHCs9fpjj5zm3rYwp1a39ZbmG9a4ELVGhBvUL7FzFoT02r7GTXdaeMe_MXKyaw)

### poke-api-consumer

[![](https://mermaid.ink/img/pako:eNqVlE1qwzAQha8itHJpcwEvCv2lEEpLuzWYQZ4kItZIlceUUHr3ypHayHFcSDaJPO896Rs58yWVbVCWssOPHknhvYa1B1ORCB8HnrXSDoiFAU0COvEcvqfVO0vsbduiHzSH1VS5hNUWgqDrTRSPHkz1j7rFJ6AmRWfLmexbb7dZsojr08Hvu47R_OaKuKwS30C8uL6-PNCUQlPHwayBMYoOxUE6YhmpC7ZOq5rA4MUpZ8Y19q1CoXbAm2QbbRGcGXMplCVCxcXy5nF5U9--vSwf3k76gnGRc3nk3ifu7CizuqhsrXXDnkOmUDvVpqZM8PKIpK9dOLKxVK-8NfW-O8XFjP2orb8JBrsO1pjb_u2OC3lFMh17omYx3SwSz9nyhk77VLxGxjmu0aV7hKYebjvnye8i6uM7WgrrkPYvx5E61hfT9P2BGmCYiT9NcGSYvVXeOayV7YnRF-4M7N6FLTCC_3O6Mfyn1-mvcQ79GdxRitRUJK9kuOAwDJowJr-GQiV5gwYrWYafDfhtJSv6Djro2b7vSMmSfY9X0tt-vZHlCtourCJpGrB_T7HRbP1znML7Yfz9AyJd5hI?type=png)](https://mermaid.live/edit#pako:eNqVlE1qwzAQha8itHJpcwEvCv2lEEpLuzWYQZ4kItZIlceUUHr3ypHayHFcSDaJPO896Rs58yWVbVCWssOPHknhvYa1B1ORCB8HnrXSDoiFAU0COvEcvqfVO0vsbduiHzSH1VS5hNUWgqDrTRSPHkz1j7rFJ6AmRWfLmexbb7dZsojr08Hvu47R_OaKuKwS30C8uL6-PNCUQlPHwayBMYoOxUE6YhmpC7ZOq5rA4MUpZ8Y19q1CoXbAm2QbbRGcGXMplCVCxcXy5nF5U9--vSwf3k76gnGRc3nk3ifu7CizuqhsrXXDnkOmUDvVpqZM8PKIpK9dOLKxVK-8NfW-O8XFjP2orb8JBrsO1pjb_u2OC3lFMh17omYx3SwSz9nyhk77VLxGxjmu0aV7hKYebjvnye8i6uM7WgrrkPYvx5E61hfT9P2BGmCYiT9NcGSYvVXeOayV7YnRF-4M7N6FLTCC_3O6Mfyn1-mvcQ79GdxRitRUJK9kuOAwDJowJr-GQiV5gwYrWYafDfhtJSv6Djro2b7vSMmSfY9X0tt-vZHlCtourCJpGrB_T7HRbP1znML7Yfz9AyJd5hI)

## Decisões de projeto

1. Arquitetura em camadas
   - Extensibilidade
   - Separação de responsabilidades (Princípio da Responsabilidade única SOLID)
   - Fácil manutenção, entendimento e testagem

2. Projetos independentes (poke-api-producer e poke-api-consumer)
   - Facilita escalabilidade indepedente (consumers e producers)
   - Robustez mitiga ponto unico de falha

3. Implementação em Python
   
4. Todos os recursos sobem a partir do mesmo docker-compose
   1. Portabilidade entre sistemas
   2. Emular ambiente de produção


## Testes



## Setup e Execução

### Requisitos

- Docker
- Docker compose

### Arquivos de configuração

- `docker-compose.yml` - Configura todos os serviços e suas respectivas dependências

### Execução

Para iniciar os serviços (Kafka, Zookeeper, poke-api-producer e poke-api-consumer), execute o seguinte comando na raiz do projeto:

#### Linux / macOS

```bash
# Executar os comandos no terminal (Bash)
make up-with-logs
```

#### Windows


```
$(docker compose up -d) ; docker compose logs --follow python-producer python-consumer
```

Para parar a execução do sistema e remover os containers basta executar:

```
docker compose down
```

ou

```
ctrl + c
```

## Qualidade de código

Visando garantir a qualidade e conformidade com padrões de código foi utilizada da ferramenta `Ruff` no processo de desenvolvimento. Por ser um linter simples, rápido e leve permite capturar erros de programação, reforçando a consistência de estilo em todo o código de maneira eficiente 


## Desafios

- Uso do Kafka
- Uso do Docker
- Integrar os serviços em um mesmo docker-compose
- Implementar CI usando GitHub Actions

## Próximos passos

- Implementação em GO
- Adicionar serviços de monitoramento e instrumentação
- Gerar imagem docker para deploy (CD)
- Uso do Ruff integrado ao CI
- Mais testes
- Persistir os dados de outra forma


## Contato


