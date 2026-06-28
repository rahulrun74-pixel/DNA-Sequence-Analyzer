import streamlit as st

from dna_analyzer import analyze_dna
from gc_content import calculate_gc
from protein_translator import translate_dna
from reverse_complement import reverse_complement
from codon_usage import codon_usage

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Bioinformatics Toolkit",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------------------------------
# Title
# -----------------------------------------------------

st.title("🧬 Bioinformatics Toolkit")
st.caption("A Python-based toolkit for DNA sequence analysis")

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

with st.sidebar:

    st.title("🧬 Toolkit")

    tool = st.radio(
        "Select a Tool",
        [
            "DNA Analyzer",
            "GC Content",
            "Protein Translator",
            "Reverse Complement",
            "Codon Usage"
        ]
    )

    st.markdown("---")

    st.info(
        """
        ### About

        **Developer:** Rahul G P

        Built using:

        - Python
        - Streamlit
        """
    )

# -----------------------------------------------------
# Input
# -----------------------------------------------------

st.header(tool)

dna = st.text_area(
    "Paste DNA Sequence",
    height=180,
    placeholder="Example:\nATGCGTAACCGT"
)

# -----------------------------------------------------
# Button
# -----------------------------------------------------

if st.button("🧬 Run Analysis", use_container_width=True):

    dna = dna.strip().upper()

    if dna == "":
        st.error("Please enter a DNA sequence.")

    # ==========================================
    # DNA Analyzer
    # ==========================================

    elif tool == "DNA Analyzer":

        result = analyze_dna(dna)

        st.subheader("Analysis Result")

        left, right = st.columns(2)

        left.metric("Sequence Length", result["length"])
        right.metric("GC Content", f"{result['gc_content']:.2f}%")

        st.write("### Nucleotide Count")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("A", result["A"])
        c2.metric("T", result["T"])
        c3.metric("G", result["G"])
        c4.metric("C", result["C"])

        if result["valid"]:
            st.success("✅ Valid DNA Sequence")
        else:
            st.error("❌ Invalid DNA Sequence")

    # ==========================================
    # GC Content
    # ==========================================

    elif tool == "GC Content":

        result = calculate_gc(dna)

        st.subheader("GC Content Result")

        st.metric("Sequence Length", result["length"])
        st.metric("GC Content", f"{result['gc_content']:.2f}%")

    # ==========================================
    # Protein Translator
    # ==========================================

    elif tool == "Protein Translator":

        protein = translate_dna(dna)

        st.subheader("Protein Sequence")

        st.code(protein)

    # ==========================================
    # Reverse Complement
    # ==========================================

    elif tool == "Reverse Complement":

        rc = reverse_complement(dna)

        st.subheader("Reverse Complement")

        st.code(rc)

    # ==========================================
    # Codon Usage
    # ==========================================

    elif tool == "Codon Usage":

        result = codon_usage(dna)

        if result is None:

            st.error("Invalid DNA Sequence")

        else:

            st.subheader("Codon Usage")

            st.table(result)
