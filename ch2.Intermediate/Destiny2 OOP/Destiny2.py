from weapon import *
def main():
    # Examples of different weapon types
    auto_rifle = AutoRifle('Origin Story', 'High-caliber kinetic auto rifle', 450, 'Kinetic')
    hand_cannon = HandCannon('Dire Promise', 'Aggressive frame hand cannon', 10, 'Kinetic')
    pulse_rifle = PulseRifle('Bygones', 'Adaptive frame pulse rifle', 3, 'Kinetic')
    scout_rifle = ScoutRifle('MIDA Multi-Tool', 'Lightweight scout rifle', '3.4x', 'Kinetic')

    heavy_machine_gun = AutoRifle('Hammerhead', 'High-impact heavy machine gun', 450, 'Heavy')
    shotgun = HandCannon('Felwinter\'s Lie', 'Precision shotgun', 6, 'Special')
    fusion_rifle = PulseRifle('Erentil FR4', 'High-impact fusion rifle', 5, 'Special')
    sniper_rifle = ScoutRifle('Beloved', 'Adaptive sniper rifle', '4.5x', 'Special')

    # Printing out the examples
    print(auto_rifle)
    print(hand_cannon)
    print(pulse_rifle)
    print(scout_rifle)
    print(heavy_machine_gun)
    print(shotgun)
    print(fusion_rifle)
    print(sniper_rifle)


if __name__ == "__main__":
    main()
