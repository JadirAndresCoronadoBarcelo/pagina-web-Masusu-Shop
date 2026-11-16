import sqlite3

conexion = sqlite3.connect("masusuDataBase.db")

cursor = conexion.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

""" CATEGORÍA: Mouses """

cursor.execute("""
INSERT INTO productos (producto, categoria, cantidad, precio, descripcion, imagen) VALUES
('Logitech G Pro X Superlight', 'Mouses', 285, 499900.00, 'Ratón inalámbrico ultraligero de nivel competitivo con sensor HERO 25K, diseño ambidiestro optimizado para eSports y una precisión milimétrica sin latencia.', 'images/productosImagenes/Mouses/Logitech G Pro X Superlight.jpg'),
('Razer DeathAdder V3 Pro', 'Mouses', 310, 529900.00, 'Ergonomía icónica perfeccionada. Cuenta con switches ópticos de tercera generación, sensor Focus Pro de 30K y un peso pluma para largas sesiones de juego.', 'images/productosImagenes/Mouses/Razer DeathAdder V3 Pro.jpg'),
('Logitech G502 HERO', 'Mouses', 390, 249900.00, 'El ratón gaming más popular del mundo. Sensor de alta precisión, 11 botones programables, sistema de pesas ajustables e iluminación RGB LIGHTSYNC.', 'images/productosImagenes/Mouses/Logitech G502 HERO.jpg'),
('HyperX Pulsefire Haste', 'Mouses', 215, 189900.00, 'Diseño tipo panal ultraligero que prioriza la velocidad de deslizamiento. Switches TTC Golden y cable flexible de malla para menor resistencia.', 'images/productosImagenes/Mouses/HyperX Pulsefire Haste.jpg'),
('SteelSeries Rival 3', 'Mouses', 240, 149900.00, 'Durabilidad de nivel superior con polímero de grado aeronáutico, sensor óptico de verdadero seguimiento 1 a 1 e iluminación RGB brillante en 3 zonas.', 'images/productosImagenes/Mouses/SteelSeries Rival 3.jpg'),
('Corsair M65 RGB Elite', 'Mouses', 330, 289900.00, 'Estructura de aluminio anodizado con sistema de peso ajustable, sensor óptico nativo de 18,000 DPI y botón de francotirador dedicado.', 'images/productosImagenes/Mouses/Corsair M65 RGB Elite.jpg'),
('Zowie EC2-C', 'Mouses', 205, 349900.00, 'Diseño ergonómico exclusivo para diestros sin necesidad de software. Tasa de refresco ajustable y cable paracord flexible ideal para FPS.', 'images/productosImagenes/Mouses/Zowie EC2-C.jpg'),
('Razer Viper Mini', 'Mouses', 375, 129900.00, 'Formato compacto y ligero diseñado para manos pequeñas o agarre de tipo garra. Switches ópticos y cable Speedflex para movimientos ágiles.', 'images/productosImagenes/Mouses/Razer Viper Mini.jpg'),
('Logitech G305 LIGHTSPEED', 'Mouses', 295, 219900.00, 'Inalámbrico de alta gama accesible. Sensor HERO de eficiencia energética excepcional con hasta 250 horas de juego continuo con una sola pila AA.', 'images/productosImagenes/Mouses/Logitech G305 LIGHTSPEED.jpg'),
('Glorious Model O', 'Mouses', 260, 269900.00, 'Diseño de panal de abeja mate que reduce peso y mejora la ventilación de la mano. Cable flexible ultraligero y deslizadores de teflón virgen.', 'images/productosImagenes/Mouses/Glorious Model O.jpg'),
('Asus ROG Gladius III', 'Mouses', 340, 389900.00, 'Conectividad trifásica (inalámbrica 2.4GHz, Bluetooth y USB). Diseño de zócalo de interruptor de ajuste rápido exclusivo de ROG.', 'images/productosImagenes/Mouses/Asus ROG Gladius III.jpg'),
('Redragon Griffin M607', 'Mouses', 400, 89900.00, 'Excelente relación calidad-precio. 7 botones programables, iluminación LED RGB personalizable y hasta 7200 DPI ajustables al vuelo.', 'images/productosImagenes/Mouses/Redragon Griffin M607.jpg'),
('Cooler Master MM711', 'Mouses', 220, 199900.00, 'Carcasa perforada ultraligera de 60 gramos, cable Ultraweave y sensor óptico PixArt de grado de juego de hasta 16000 DPI.', 'images/productosImagenes/Mouses/Cooler Master MM711.jpg'),
('Fantech X17 Blake', 'Mouses', 310, 79900.00, 'Ratón ergonómico para juegos con memoria integrada, switches Huano de alta durabilidad y software de personalización macro dedicado.', 'images/productosImagenes/Mouses/Fantech X17 Blake.jpg'),
('Trust GXT 131 Ravan', 'Mouses', 270, 99900.00, 'Iluminación LED completa con patrones ajustables, botones laterales de fácil alcance y velocidad seleccionable sobre la marcha.', 'images/productosImagenes/Mouses/Trust GXT 131 Ravan.jpg'),
('Logitech G903 HERO', 'Mouses', 230, 459900.00, 'Diseño ambidiestro de rendimiento profesional compatible con carga inalámbiaca Powerplay, switches mecánicos y 11 botones configurables.', 'images/productosImagenes/Mouses/Logitech G903 HERO.jpg');
""")

""" CATEGORÍA: Teclados """

cursor.execute("""
INSERT INTO productos (producto, categoria, cantidad, precio, descripcion, imagen) VALUES
('Logitech G Pro X', 'Teclados', 250, 489900.00, 'Teclado mecánico tenເລks (sin teclado numérico) con switches intercambiables de nivel profesional y diseño compacto para torneos.', 'images/productosImagenes/Teclados/Logitech G Pro X.jpg'),
('Razer Huntsman Mini', 'Teclados', 320, 399900.00, 'Teclado formato 60% con switches ópticos lineales Razer. Activación a la velocidad de la luz y teclas PBT de doble inyección.', 'images/productosImagenes/Teclados/Razer Huntsman Mini.jpg'),
('HyperX Alloy Origins', 'Teclados', 380, 369900.00, 'Cuerpo de aluminio aeronáutico totalmente resistente, switches mecánicos HyperX de corto recorrido y retroiluminación RGB deslumbrante.', 'images/productosImagenes/Teclados/HyperX Alloy Origins.jpg'),
('Corsair K95 RGB Platinum XT', 'Teclados', 210, 799900.00, 'La cúspide de los teclados mecánicos. Switches Cherry MX Speed, 6 teclas macro dedicadas con integración Elgato Stream Deck y reposamuñecas.', 'images/productosImagenes/Teclados/Corsair K95 RGB Platinum XT.jpg'),
('SteelSeries Apex Pro', 'Teclados', 290, 749900.00, 'Switches mecánicos ajustables OmniPoint. Permite regular la distancia de actuación de cada tecla de forma individual de 0.4mm a 3.6mm.', 'images/productosImagenes/Teclados/SteelSeries Apex Pro.jpg'),
('Redragon Kumara K552', 'Teclados', 400, 159900.00, 'El rey de la gama de entrada. Mecánico 80% (TKL), switches Outemu Red o Blue, chasis de acero resistente y diseño antisalpicaduras.', 'images/productosImagenes/Teclados/Redragon Kumara K552.jpg'),
('Keychron K2 V2', 'Teclados', 270, 349900.00, 'Teclado mecánico inalámbrico formato 75% compatible tanto con Windows como con Mac. Conectividad Bluetooth multidispositivo.', 'images/productosImagenes/Teclados/Keychron K2 V2.jpg'),
('Asus ROG Strix Scope RX', 'Teclados', 230, 519900.00, 'Switches óptico-mecánicos ROG RX exclusivos. Estabilidad superior en cada pulsación, resistencia al agua IP56 y tecla Ctrl ancha para FPS.', 'images/productosImagenes/Teclados/Asus ROG Strix Scope RX.jpg'),
('Logitech G915 LIGHTSPEED', 'Teclados', 205, 849900.00, 'Teclado mecánico inalámbrico de perfil bajo. Switches de bajo perfil GL, conectividad ultrarrápida y controles multimedia dedicados de aluminio.', 'images/productosImagenes/Teclados/Logitech G915 LIGHTSPEED.jpg'),
('Razer BlackWidow V3', 'Teclados', 310, 429900.00, 'El legado continúa. Switches mecánicos verdes con respuesta táctil y sonora, marco de aluminio y reposamuñecas ergonómico afelpado.', 'images/productosImagenes/Teclados/Razer BlackWidow V3.jpg'),
('Redragon Brahma K586', 'Teclados', 340, 279900.00, 'Teclado mecánico completo con rueda de volumen metálica dedicada, 10 teclas macro y reposamuñecas magnético de gran comodidad.', 'images/productosImagenes/Teclados/Redragon Brahma K586.jpg'),
('Cougar Puri TKL', 'Teclados', 225, 259900.00, 'Diseñado para eSports. Incluye cubierta magnética protectora para transportarlo sin daños y un sistema inteligente de gestión de cables.', 'images/productosImagenes/Teclados/Cougar Puri TKL.jpg'),
('Epomaker EP84', 'Teclados', 285, 389900.00, 'Teclado mecánico compacto con diseño estético moderno, teclas PBT de alta calidad e iluminación RGB dinámica totalmente programable.', 'images/productosImagenes/Teclados/Epomaker EP84.jpg'),
('Trust GXT 835 Azor', 'Teclados', 390, 99900.00, 'Teclado de tamaño completo con luces LED de colores combinados, función anti-ghosting de hasta 8 pulsaciones simultáneas y modo juego.', 'images/productosImagenes/Teclados/Trust GXT 835 Azor.jpg'),
('Motospeed K87S', 'Teclados', 300, 179900.00, 'Teclado mecánico retroiluminado con efectos RGB laterales envolventes, switches mecánicos duraderos y estructura compacta.', 'images/productosImagenes/Teclados/Motospeed K87S.jpg'),
('Royal Kludge RK61', 'Teclados', 350, 189900.00, 'Teclado inalámbrico 60% con conectividad Bluetooth y modo cableado USB-C. Batería de larga duración y switches intercambiables hot-swap.', 'images/productosImagenes/Teclados/Royal Kludge RK61.jpg');
""")

""" CATEGORÍA: Diademas """

cursor.execute("""
INSERT INTO productos (producto, categoria, cantidad, precio, descripcion, imagen) VALUES
('HyperX Cloud II', 'Diademas', 395, 349900.00, 'La diadema gamer por excelencia. Sonido envolvente virtual 7.1, comodidad legendaria con espuma viscoelástica y micrófono desmontable.', 'images/productosImagenes/Diademas/HyperX Cloud II.jpg'),
('Logitech G733 LIGHTSPEED', 'Diademas', 270, 489900.00, 'Auriculares inalámbricos ligeros y coloridos. Diadema de suspensión ajustable, iluminación frontal DTS Headphone:X 2.0 y filtros de voz.', 'images/productosImagenes/Diademas/Logitech G733 LIGHTSPEED.jpg'),
('Razer BlackShark V2 Pro', 'Diademas', 240, 599900.00, 'Audio inalámrico de nivel profesional para esports. Drivers TriForce de titanio de 50 mm y cancelación pasiva de ruido avanzada.', 'images/productosImagenes/Diademas/Razer BlackShark V2 Pro.jpg'),
('SteelSeries Arctis Nova 7', 'Diademas', 215, 629900.00, 'Sistema de audio acústico Nova con drivers de alta fidelidad. Conectividad inalámbrica simultánea de 24GHz y Bluetooth para llamadas.', 'images/productosImagenes/Diademas/SteelSeries Arctis Nova 7.jpg'),
('Corsair Void RGB Elite', 'Diademas', 310, 319900.00, 'Construcción de malla de microfibra transpirable con almohadillas de espuma viscoelástica y sonido envolvente 7.1 inmersivo en PC.', 'images/productosImagenes/Diademas/Corsair Void RGB Elite.jpg'),
('Logitech G Pro X Wireless', 'Diademas', 200, 719900.00, 'Tecnología de voz BLUE VO!CE, conectividad inalámbrica LIGHTSPEED de alta velocidad y un diseño robusto de acero y aluminio.', 'images/productosImagenes/Diademas/Logitech G Pro X Wireless.jpg'),
('Redragon H510 Zeus', 'Diademas', 380, 169900.00, 'Sonido envolvente 7.1 con almohadillas de espuma viscoelástica de gran tamaño. Compatible multiplataforma (PC, consolas y dispositivos móviles).', 'images/productosImagenes/Diademas/Redragon H510 Zeus.jpg'),
('JBL Quantum 400', 'Diademas', 330, 289900.00, 'Tecnología JBL QuantumSOUND Signature para una inmersión realista total. Micrófono direccional abatible con función de silencio.', 'images/productosImagenes/Diademas/JBL Quantum 400.jpg'),
('Razer Kraken X', 'Diademas', 400, 149900.00, 'Ultraligeras con apenas 250 gramos de peso. Sonido envolvente 7.1 claro y preciso con almohadillas de espuma suave para uso prolongado.', 'images/productosImagenes/Diademas/Razer Kraken X.jpg'),
('Audio-Technica ATH-GDL3', 'Diademas', 220, 549900.00, 'Auriculares gaming de diseño abierto ultraligeros que ofrecen un campo sonoro natural y espacioso, ideales para sesiones largas.', 'images/productosImagenes/Diademas/Audio-Technica ATH-GDL3.jpg'),
('Asus ROG Delta S', 'Diademas', 255, 689900.00, 'DAC cuádruple ESS de alta fidelidad para un audio impecablemente detallado. Micrófono con cancelación de ruido asistida por IA.', 'images/productosImagenes/Diademas/Asus ROG Delta S.jpg'),
('Turtle Beach Recon 500', 'Diademas', 290, 229900.00, 'Drivers duales de 60 mm pioneros en la industria para ofrecer frecuencias altas y bajas separadas con una nitidez asombrosa.', 'images/productosImagenes/Diademas/Turtle Beach Recon 500.jpg'),
('Logitech G435 LIGHTSPEED', 'Diademas', 360, 269900.00, 'Auriculares ecológicos ultraligeros con conectividad Bluetooth y USB inalámbrico. Diseños modernos y fabricados con plástico reciclado.', 'images/productosImagenes/Diademas/Logitech G435 LIGHTSPEED.jpg'),
('HyperX Cloud Stinger 2', 'Diademas', 375, 189900.00, 'Evolución de un clásico. Ligeros, orejeras con giro de 90 grados y sonido nítido para mejorar la experiencia de juego diaria.', 'images/productosImagenes/Diademas/HyperX Cloud Stinger 2.jpg'),
('Fantech HG28 Portal', 'Diademas', 310, 89900.00, 'Diadema económica con iluminación RGB sutil, diseño cómodo de diadema suspendida y micrófono integrado para chat de voz claro.', 'images/productosImagenes/Diademas/Fantech HG28 Portal.jpg'),
('Sennheiser EPOS H3', 'Diademas', 205, 459900.00, 'Ingeniería acústica de alta gama enfocada en la claridad de audio competitiva y comodidad ergonómica superior.', 'images/productosImagenes/Diademas/Sennheiser EPOS H3.jpg');
""")

""" CATEGORÍA: Sillas """

cursor.execute("""
INSERT INTO productos (producto, categoria, cantidad, precio, descripcion, imagen) VALUES
('Secretlab Titan Evo 2022', 'Sillas', 205, 2199900.00, 'La cúspide en ergonomía y confort gaming. Cuero sintético híbrido Neo™ or Neo-Bliss, soporte lumbar ajustable integrado de 4 direcciones.', 'images/productosImagenes/Sillas/Secretlab Titan Evo 2022.jpg'),
('Corsair T3 Rush', 'Sillas', 240, 1299900.00, 'Inspirada en los asientos de los coches de carreras. Exterior de tela suave y transpirable, cojín cervical y soporte lumbar de espuma viscoelástica.', 'images/productosImagenes/Sillas/Corsair T3 Rush.jpg'),
('Razer Iskur', 'Sillas', 220, 1899900.00, 'Diseñada para un juego hardcore con soporte lumbar esculpido único. Cojines de espuma de alta densidad y reposabrazos 4D totalmente ajustables.', 'images/productosImagenes/Sillas/Razer Iskur.jpg'),
('ThunderX3 BC3', 'Sillas', 350, 799900.00, 'Tecnología AIR Tech para mayor transpirabilidad. Cuero sintético con patrón de carbono, reposabrazos ajustables y cojines de soporte incluidos.', 'images/productosImagenes/Sillas/ThunderX3 BC3.jpg'),
('Cougar Armor One', 'Sillas', 310, 899900.00, 'Estructura de acero robusta con diseño ergonómico, reclinación de hasta 180 grados y almohadas adicionales para cabeza y zona lumbar.', 'images/productosImagenes/Sillas/Cougar Armor One.jpg'),
('Asus ROG Chariot SL300', 'Sillas', 210, 1999900.00, 'Estética profesional de alta gama con soporte lumbar de espuma viscoelástica, reposabrazos 4D y cómoda correa trasera para colgar accesorios.', 'images/productosImagenes/Sillas/Asus ROG Chariot SL300.jpg'),
('Aerocool Duke', 'Sillas', 290, 859900.00, 'Diseño elegante con detalles en fibra de carbono y superficie perforada transpirable que mantiene la frescura durante todo el día.', 'images/productosImagenes/Sillas/Aerocool Duke.jpg'),
('Caliber R2C Cooler Master', 'Sillas', 260, 1199900.00, 'Tapizado con tela especial con tecnología de refrigeración avanzada que reduce la acumulación de calor corporal y humedad.', 'images/productosImagenes/Sillas/Caliber R2C Cooler Master.jpg'),
('XTRIKE ME GC-905', 'Sillas', 380, 549900.00, 'Silla gamer económica con diseño deportivo ergonómico, altura ajustable por gas y respaldo reclinable para máxima relajación.', 'images/productosImagenes/Sillas/XTRIKE ME GC-905.jpg'),
('Vertagear SL4000', 'Sillas', 230, 1499900.00, 'Construcción con aleación de metal resistente, acolchado de espuma de alta densidad que resiste la deformación con el paso de los años.', 'images/productosImagenes/Sillas/Vertagear SL4000.jpg'),
('Noblechairs Hero', 'Sillas', 200, 2099900.00, 'Diseño sofisticado enfocado en usuarios exigentes. Gran superficie de asiento y respaldo con soporte lumbar integrado ajustable.', 'images/productosImagenes/Sillas/Noblechairs Hero.jpg'),
('AKRacing Core Series EX', 'Sillas', 270, 1399900.00, 'Tela de alta calidad suave al tacto y fácil de limpiar. Estructura metálica duradera con garantía de rendimiento a largo plazo.', 'images/productosImagenes/Sillas/AKRacing Core Series EX.jpg'),
('ErgoChair Pro (Autonomous)', 'Sillas', 215, 1799900.00, 'Silla de oficina ergonómica avanzada con respaldo de malla transpirable, inclinación ajustable y soporte dinámico para postura correcta.', 'images/productosImagenes/Sillas/ErgoChair Pro (Autonomous).jpg'),
('Gamemax BlackRed', 'Sillas', 390, 649900.00, 'Excelente equilibrio entre coste y rendimiento. Diseño agresivo gamer en tonos negro y rojo con pistón de elevación de clase 4.', 'images/productosImagenes/Sillas/Gamemax BlackRed.jpg'),
('Herman Miller Embody', 'Sillas', 200, 4999900.00, 'La silla ergonómica definitiva diseñada por médicos. Pixelated Support que se adapta instantáneamente a cada micromovimiento del cuerpo.', 'images/productosImagenes/Sillas/Herman Miller Embody.jpg'),
('Msi MAG CH120', 'Sillas', 320, 1099900.00, 'Estructura de acero pintado anticorrosión, espuma moldeada de alta densidad y ruedas con freno para evitar deslizamientos imprevistos.', 'images/productosImagenes/Sillas/Msi MAG CH120.jpg');
""")

conexion.commit()