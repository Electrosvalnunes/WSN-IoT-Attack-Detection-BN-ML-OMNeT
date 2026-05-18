package wsn36;

// Topologia experimental com 36 nós sensores + 1 nó sink.
// Compatível com a lógica metodológica descrita no artigo:
// área 400 m x 400 m, grade 6 x 6, espaçamento aproximado de 80 m,
// sink no centro da rede e tráfego UDP dos sensores para o sink.

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.WirelessHost;
import inet.physicallayer.wireless.ieee802154.packetlevel.Ieee802154NarrowbandScalarRadioMedium;
import inet.visualizer.canvas.integrated.IntegratedCanvasVisualizer;

network WSN36_Grid_Topology
{
    parameters:
        int numSensors = default(36);
        @display("bgb=650,520");

    submodules:
        visualizer: IntegratedCanvasVisualizer {
            @display("p=70,40");
        }
        configurator: Ipv4NetworkConfigurator {
            @display("p=70,100");
        }
        radioMedium: Ieee802154NarrowbandScalarRadioMedium {
            @display("p=70,160");
        }
        sink: WirelessHost {
            @display("p=325,260;i=device/server");
        }
        sensor[numSensors]: WirelessHost {
            @display("i=misc/sensor");
        }
}
