PROJETO: WSN36_OMNeT_Project_CPP
Objetivo: adicionar módulos C++ de ataques ao cenário OMNeT++/INET com 36 nós.

ARQUIVOS PRINCIPAIS
1. WSN36_Grid_Topology.ned
   Topologia com 36 sensores + 1 sink.

2. AttackApps.ned
   Declaração dos módulos C++:
   - MaliciousFloodingApp
   - AggressiveBackoffApp
   - BlackholeUdpDropApp
   - WormholeEndpointApp

3. omnetpp.ini
   Configurações dos cenários:
   - Normal
   - Flooding
   - Backoff
   - Blackhole
   - Wormhole

4. src/*.cc e src/*.h
   Implementação C++ dos módulos.

COMO INTRODUZIR NO OMNeT++ IDE
1. Abra o OMNeT++.
2. File > New > OMNeT++ Project.
3. Dê o nome: WSN36_OMNeT_Project_CPP.
4. Marque Empty Project.
5. Copie para dentro do projeto:
   - WSN36_Grid_Topology.ned
   - AttackApps.ned
   - omnetpp.ini
   - pasta src
6. Clique com botão direito no projeto > Properties > Project References.
7. Marque o projeto INET.
8. Clique com botão direito no projeto > Build Project.
9. Execute o omnetpp.ini e escolha o cenário desejado.

SE O PROJETO NÃO COMPILAR AUTOMATICAMENTE
No terminal do OMNeT++, dentro da pasta do projeto, use:

opp_makemake -f --deep -I../inet/src -L../inet/src -lINET
make MODE=debug all

Observação: o caminho ../inet/src pode mudar conforme o nome/pasta onde o INET foi instalado.

CENÁRIOS
- Normal: tráfego UDP regular.
- Flooding: sensor[0] envia pacotes de 119 B a cada 0.12 s.
- Backoff: sensor[25] usa tráfego agressivo para representar contenção manipulada.
- Blackhole: sensor[5] descarta pacotes UDP recebidos e registra blackholeDroppedPackets.
- Wormhole: sensor[25] e sensor[15] criam túnel UDP artificial.

NOTA METODOLÓGICA IMPORTANTE
Estes módulos implementam os ataques em nível de aplicação/experimento, compatíveis com INET.
Para Blackhole, Wormhole e Backoff totalmente internos ao RPL/MAC, é necessário alterar módulos internos do INET, como o encaminhamento IP/RPL ou o CSMA/CA MAC. Isso é mais invasivo e depende exatamente da versão do INET.
