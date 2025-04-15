from streamlit_agraph import agraph, Node, Edge, Config
import streamlit as st

st.set_page_config(layout="wide")
st.title("🛍️ Flowchart Analisa Sales 2025")

# === Layout Columns ===
col1, col2 = st.columns([3, 1])

# === Define Nodes with IDs (keep IDs simple) ===
nodes = [
    Node(id="a", label="   1. Forecast & POB Submit   ", shape="box", color="#cfe2ff", x=-300, y=-100, font={"size": 32}),
    Node(id="b", label="   2. POB & POM Pengiriman + AO", shape="box", color="#cfe2ff", x=300, y=-100, font={"size": 32}),
    Node(id="c", label="   3. Renpro   ", shape="box", color="#cfe2ff", x=-300, y=50, font={"size": 32}),
    Node(id="d", label="   4. POB & POM Produksi   ", shape="box", color="#cfe2ff", x=-300, y=300, font={"size": 32}),
    Node(id="e", label="   5. Real  ", shape="box", color="#cfe2ff", x=-300, y=500, font={"size": 32}),
    Node(id="i", label="   6. Sisa Stock   ", shape="eclipse", color="yellow", x=-300, y=600, font={"size": 26}),
    Node(id="f", label="   7. Pengiriman (SO +SJ)  ", shape="box", color="#cfe2ff", x=300, y=500, font={"size": 32}),
    Node(id="g", label="   8. Sisa Pengiriman (Outstanding Pengiriman)   ", shape="ellipse", color="yellow", x=300, y=700, font={"size": 32}),
    Node(id="h", label="   Buffer Sisa Pengriman dari POB Submit   ", shape="ellipse", color="yellow", x=-300, y=800, font={"size": 26}),
    Node(id="EndFlow", label="% Growth", shape="ellipse", color="red", x=0, y=1000, font={"size": 50, "color": "white"}),
    Node(id="overall", label="% Achivement atau Potensi Kendala", shape="ellipse", color="red", x=-900, y=300, font={"size": 24, "color": "white"}),
    Node(id="overall2", label="% Achivement atau Potensi Kendala", shape="ellipse", color="red", x=200, y=150, font={"size": 24, "color": "white"}),
    Node(id="overall3", label="% Achivement atau Potensi Kendala", shape="ellipse", color="red", x=600, y=600, font={"size": 24, "color": "white"}),

]
# === Define Edges ===
edges = [
    Edge(source="a", target="b"),
    Edge(source="b", target="c"),
    Edge(source="c", target="d"),
    Edge(source="d", target="e"),
    Edge(source="e", target="f"),
    Edge(source="f", target="g"),
    Edge(source="i", target="h"),
    Edge(source="e", target="i"),
    #untuk potensi kendala
    Edge(source="a", target="overall", color = "red", arrows = "none", smooth={"enabled": True, "type": "cubicBezier", "roundness": 1.1}),
    Edge(source="overall", target="h", color = "red", arrows = "none", smooth={"enabled": True, "type": "cubicBezier", "roundness": 1.1}),

    Edge(source="c", target="overall2", color = "red", arrows = "none", smooth={"enabled": True, "type": "cubicBezier", "roundness": 1.1}),
    Edge(source="overall2", target="d", color = "red", arrows = "none", smooth={"enabled": True, "type": "cubicBezier", "roundness": 1.1}),

    Edge(source="f", target="overall3", color = "red", arrows = "none", smooth={"enabled": True, "type": "cubicBezier", "roundness": 1.1}),
    Edge(source="overall3", target="g", color = "red", arrows = "none", smooth={"enabled": True, "type": "cubicBezier", "roundness": 1.1}),

 
]

# === AGraph Configuration ===
config = Config(
    width=1100,
    height=1000,
    directed=True,
    physics=False,  # Tetap stabil (non-draggable)
    zoom=True,
    hierarchical=False,  # Bebas posisi, tidak dipaksa ke bawah
    nodeHighlightBehavior=True
)

# === Display Graph ===
with col1:
    selected = agraph(nodes=nodes, edges=edges, config=config)

# === Keterangan Langkah ===
with col2:
    if selected:
        selected_node_id = selected  # ← langsung assign ID-nya
        
        st.markdown(f"**Keterangan/Informasi**:")

        explanations = {
            "a": "Melakukan Peramalan pada POB",
            "b": "Analisa POB & POM Pengiriman + AO",
            "c": "Analisa Renpro",
            "d": "Analisa POB & POM Produksi",
            "e": "Realisasi dari sales",
            "f": "Monitoring dan analisa Pengiriman SO + SJ",
            "g": "Sisa pengiriman yang ada",
            "h": "Sisa pengiriman stock + buffer",
            "i": "Sisa stock yang ada",
            "EndFlow": "Harapan Rate Pertumbuhan Sales",
        }

        explanation = explanations.get(selected_node_id, "ℹ️ Apakah mangalami potens kendala dalam flow proses tersebut atau justru % achivemenet.")
        st.write(explanation)
    else:
        st.info("Klik salah satu langkah pada diagram di kiri untuk melihat keterangannya.")
