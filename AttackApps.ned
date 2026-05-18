package wsn36;

// Módulos C++ de ataque para a metodologia com 36 sensores.
// Estes módulos são aplicações UDP maliciosas compatíveis com os hosts do INET.
// São usados em sensor[*].app[k].typename no omnetpp.ini.

import inet.applications.contract.IApp;

simple MaliciousFloodingApp like IApp
{
    parameters:
        string destAddress;
        int destPort;
        int localPort = default(-1);
        int packetLength @unit(B) = default(119B);
        volatile double sendInterval @unit(s) = default(0.12s);
        double startTime @unit(s) = default(20s);
        double stopTime @unit(s) = default(250s);
        @class(wsn36::MaliciousFloodingApp);
        @display("i=block/source");
    gates:
        input socketIn;
        output socketOut;
}

simple AggressiveBackoffApp like IApp
{
    parameters:
        string destAddress;
        int destPort;
        int localPort = default(-1);
        int packetLength @unit(B) = default(48B);
        volatile double sendInterval @unit(s) = default(0.05s);
        double startTime @unit(s) = default(200s);
        double stopTime @unit(s) = default(250s);
        @class(wsn36::AggressiveBackoffApp);
        @display("i=block/source");
    gates:
        input socketIn;
        output socketOut;
}

simple BlackholeUdpDropApp like IApp
{
    parameters:
        int localPort = default(5000);
        double startTime @unit(s) = default(200s);
        double stopTime @unit(s) = default(250s);
        @class(wsn36::BlackholeUdpDropApp);
        @display("i=block/sink");
    gates:
        input socketIn;
        output socketOut;
}

simple WormholeEndpointApp like IApp
{
    parameters:
        string peerAddress;
        int peerPort = default(7000);
        int localPort = default(7000);
        string finalDestAddress = default("sink");
        int finalDestPort = default(5000);
        int packetLength @unit(B) = default(48B);
        volatile double sendInterval @unit(s) = default(0.07s);
        double startTime @unit(s) = default(200s);
        double stopTime @unit(s) = default(250s);
        bool generateAttackTraffic = default(true);
        @class(wsn36::WormholeEndpointApp);
        @display("i=block/routing");
    gates:
        input socketIn;
        output socketOut;
}
