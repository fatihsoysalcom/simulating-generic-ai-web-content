import random

def generate_ai_like_paragraph(num_sentences=3):
    """
    Generates a paragraph simulating generic, AI-like content.
    This demonstrates the potential for repetitive and unoriginal text
    that the article warns against, contributing to an "AI soup."
    """
    starters = [
        "Günümüz dijital çağında,",
        "Yapay zeka teknolojileri hızla gelişirken,",
        "Web'in evrimiyle birlikte,",
        "Modern internet deneyiminde,",
        "Kullanıcı deneyimini optimize etmek adına,"
    ]
    middles = [
        "içerik üretim süreçleri önemli bir dönüşüm geçirmektedir.",
        "bilgiye erişim ve etkileşim biçimleri yeniden tanımlanmaktadır.",
        "algoritmik yaklaşımlar kritik bir rol oynamaktadır.",
        "veri analizi ve otomasyon kapasiteleri artmaktadır.",
        "dijital ekosistem sürekli olarak evrilmektedir."
    ]
    endings = [
        "Bu durum, yeni fırsatlar sunarken beraberinde zorlukları da getirmektedir.",
        "Önemli olan, dengeli bir yaklaşım sergilemektir.",
        "Sürdürülebilir çözümler geliştirmek esastır.",
        "Kullanıcı odaklı stratejiler benimsemek gereklidir.",
        "Geleceğin web'i için bu analizler değerlidir."
    ]

    paragraph = []
    for _ in range(num_sentences):
        sentence = (
            random.choice(starters) + " " +
            random.choice(middles) + " " +
            random.choice(endings)
        )
        paragraph.append(sentence)
    return " ".join(paragraph) + "\n"

def generate_human_like_paragraph():
    """
    Generates a more specific, coherent, and unique paragraph,
    representing content that aims for originality and depth.
    """
    return (
        "Birkaç gün önce, yerel bir kafede otururken, yan masadaki iki genç "
        "yazılımcının yapay zeka destekli içeriklerin web'i nasıl etkilediğini "
        "tartıştıklarını duydum. Biri, 'Her şey aynılaşmaya başladı, özgün bir şey "
        "bulmak zor,' derken, diğeri 'Ama hız ve verimlilik de önemli,' diye "
        "karşı çıktı. Bu sohbet, makalede ele aldığımız endişeleri somut bir "
        "şekilde yansıtıyordu. Gerçekten de, bilgiye ulaşırken sadece "
        "derinliksiz bir 'çorba' ile mi karşılaşacağız, yoksa yapay zeka "
        "araçlarını yaratıcılığı desteklemek için mi kullanacağız? Bu, "
        "önümüzdeki en büyük sorulardan biri."
    ) + "\n"

if __name__ == "__main__":
    print("--- Yapay Zeka Tarafından Üretilmiş Gibi Görünen İçerik ---")
    print("Bu bölüm, yapay zekanın üretebileceği potansiyel olarak genel ve tekrarlayıcı metinleri simüle eder.")
    print("Makalenin 'kullanılamaz yapay zeka çorbası' endişesini göstermektedir.\n")

    for i in range(3): # Generate a few AI-like paragraphs
        print(f"Paragraf {i+1}:")
        print(generate_ai_like_paragraph())
        # Inline comment: This paragraph demonstrates the generic, often repetitive nature
        # of some AI-generated content, which the article suggests can make the web "unusable."

    print("\n--- İnsan Tarafından Yazılmış Gibi Görünen İçerik ---")
    print("Bu bölüm, daha özgün, bağlam odaklı ve derinlemesine bir insan yazısını temsil eder.")
    print("Yapay zeka içeriğinin aksine, kişisel bir bakış açısı ve spesifik detaylar içerir.\n")

    print(generate_human_like_paragraph())
    # Inline comment: This paragraph aims to show the contrast with human-generated content,
    # which often provides unique insights, specific examples, and a distinct voice,
    # qualities that the article suggests might be lost in an "AI soup."

    print("\n--- Sonuç ---")
    print("Bu örnek, yapay zeka destekli içeriklerin web'in özgünlüğünü ve derinliğini nasıl etkileyebileceğine dair bir fikir vermektedir.")
    print("Makalenin ana fikri, bu tür içeriklerin aşırıya kaçması durumunda web'in 'kullanılamaz' hale gelebileceğidir.")
