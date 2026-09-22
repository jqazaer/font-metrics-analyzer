# Font Metrological Analyzer & Cascading Baselines Study

A metrological and anatomical study examining the vertical metrics and coordinate spaces of **IBM Plex Sans** (Latin) and **IBM Plex Sans Arabic**, backed by automated FontTools extraction and structural baseline analysis.

---

## Visual Rhythm & Structural Anatomy

The comparative analysis addresses the fundamental architectural difference between the rigid horizontal Latin baseline ($y=0$) and the dynamic cascading baseline system inherent to Arabic Nastaliq/Naskh typography (based on Thomas Milo's DecoType research).

![Contextual Rhythm and Cascading Baselines](assets/baseline_rhythm_diagram.png)

### Key Structural Baselines:
- **$B_3$ — Cascading Baseline 3 (Elevated):** Elevated secondary baseline accommodating ascending glyph bodies, nested kafs (`ك`), and stacked character connections.
- **$B_2$ — Primary Baseline (Main):** Main sitting baseline establishing line-level visual coherence.
- **$B_1$ — Cascading Baseline 1 (Sub-level):** Deep landing baseline accommodating descender bowls (Nun, Ra, Qaf) and low ligature connections.
- **Dynamic Baseline Connections:** Multi-tier fluid transit links bridging cascading letters across words.

---

## Comparative OpenType Metrology

Extracted using `extract_metrics.py` via `fontTools`:

| المعيار المترولوجي (OpenType Metric) | النسق اللاتيني (IBM Plex Sans) | النسق العربي (IBM Plex Sans Arabic) | الدلالة الهندسية والتصميمية |
| :--- | :---: | :---: | :--- |
| **قيمة مربع الـ Em الأساسية** (`unitsPerEm`) | `1000` | `1000` | فضاء الإحداثيات المشترك للخطين داخل الملف الرقمي لتوحيد مقياس الرسم. |
| **صاعد جدول الماك** (`hhea.ascender`) | `1025` | `1085` | مقياس الصاعد على مستوى نظام Apple لتفادي تفاوت ارتفاع السطر في Safari/WebKit. |
| **هابط جدول الماك** (`hhea.descender`) | `-275` | `-415` | عمق الهبوط المخصص لاستيعاب الكؤوس العميقة والمنحدرات السفلية. |
| **الفجوة السطرية لجدول الماك** (`hhea.lineGap`) | `0` | `0` | تصفير الفجوة يلزم البيئات الرقمية بعدم توليد هوامش عشوائية غير منضبطة. |
| **راية المقاييس الطباعية** (`fsSelection` bit 7) | `Enabled (1)` | `Enabled (1)` | تفعيل `USE_TYPO_METRICS` لإجبار التطبيقات الحديثة على اعتماد قيم `sTypo` وتجاهل `usWin`. |
| **صاعد الخط الطباعي** (`sTypoAscender`) | `1025` | `1085` | يمتد الصاعد العربي بنسبة أكبر لاستيعاب حركات التشكيل العلوية المركبة والهمزات. |
| **هابط الخط الطباعي** (`sTypoDescender`) | `-275` | `-415` | امتداد سفلي إضافي في العربي لاستيعاب كؤوس الراء والنون والقاف وعلامات الكسر. |
| **الفجوة السطرية الطباعية** (`sTypoLineGap`) | `0` | `0` | تصفير الفجوة لترك التحكم في التباعد الرأسي لقيم الصاعد والهابط الفعلية. |
| **إجمالي الميزانية الرأسية** (`Typo Total`) | `1300` | `1500` | الميزانية الكلية للسطر (`Ascender - Descender + LineGap`)، تمنح العربي مساحة رأسية أوسع لاستيعاب التراكب. |
| **سقف ويندوز الآمن** (`usWinAscent`) | `1120` | `1128` | حد القطع في Windows GDI لتفادي بتر حركات التشكيل المركبة (`mark-to-mark`). |
| **قاع ويندوز الآمن** (`usWinDescent`) | `275` | `601` | زيادة هامش القاع الآمن بنسبة ملحوظة لحماية النقاط السفلية وتنوين الكسر من البتر. |
| **ارتفاع الحرف الصغير** (`sxHeight`) | `515` | `Undefined` / شكلي | مرجع بنيوي لاتيني خالص؛ محاولة مطابقة أسنان الحروف العربية معه تقود إلى تسطيح حركتها. |
| **ارتفاع الحرف الكبير** (`sCapHeight`) | `698` | `698` (مرجعي) | كبح صواعد الألف واللام لموازاتها بصرياً مع سقف الحرف اللاتيني الكبير داخل العائلة. |

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- `pip` package manager

### 1. Clone the repository
```bash
git clone https://github.com/USERNAME/font-metrics-analyzer.git
cd font-metrics-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add font files
Place your `.ttf` or `.otf` files into the `fonts/` directory:
- `fonts/IBMPlexSans-Regular.ttf`
- `fonts/IBMPlexSansArabic-Regular.ttf`

---

## Usage

### Run Default Inspection
Inspect the pair of IBM Plex fonts configured by default:
```bash
python extract_metrics.py
```

### Inspect Custom Font Files
You can pass any font file directly via command-line arguments:
```bash
python extract_metrics.py path/to/MyFont-Regular.ttf path/to/AnotherFont.otf
```

---

## File Structure

```text
font-metrics-analyzer/
├── fonts/
│   ├── README.md
│   ├── .gitkeep
│   ├── IBMPlexSans-Regular.ttf          <- Add here
│   └── IBMPlexSansArabic-Regular.ttf    <- Add here
├── assets/
│   └── baseline_rhythm_diagram.png     <- Annotated structural anatomy diagram
├── extract_metrics.py                   <- FontTools extraction script
├── requirements.txt                     <- Project dependencies
├── .gitignore                           <- Git ignore rules
├── LICENSE                              <- MIT License
└── README.md                            <- Repository documentation
```

---

## License

This project is licensed under the [MIT License](LICENSE).  
The IBM Plex font family is released by IBM under the [SIL Open Font License](http://scripts.sil.org/OFL).
