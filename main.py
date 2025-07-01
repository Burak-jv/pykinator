print(">> Program başlatılıyor...")

from engine import AkinatorEngine
from utils import load_knowledge, save_knowledge

def main():
    print("Akinator'a hoş geldin! Aklındaki karakteri tahmin etmeye çalışacağım.\n")
    
    knowledge = load_knowledge("database/dat.json")
    engine = AkinatorEngine(knowledge)

    result = engine.play()

    if result:
        print(f"\nTahminim: {result}! Doğru mu?")
        cevap = input("(evet/hayır): ").strip().lower()
        if cevap == "evet":
            print("Harika! Bildim :)")
        else:
            print("O zaman öğret bana!")
            karakter = input("Karakterin adı neydi?: ").strip()
            engine.learn_new_character(karakter)
    else:
        print("\nTahmin edemedim. Lütfen karakterini öğret bana!")
        karakter = input("Karakterin adı neydi?: ").strip()
        engine.learn_new_character(karakter)

    save_knowledge("database/dat.json", engine.knowledge)

if __name__ == "__main__":
    main()
