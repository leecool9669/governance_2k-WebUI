# -*- coding: utf-8 -*-
"""GovernanceBERT-governance 文本分类 WebUI 演示（不加载真实模型权重）。"""
from __future__ import annotations

import gradio as gr


def fake_load_model():
    """模拟加载模型，实际不下载权重，仅用于界面演示。"""
    return "模型状态：GovernanceBERT-governance 已就绪（演示模式，未加载真实权重）"


def fake_classify(text: str) -> tuple[str, str]:
    """模拟治理文本分类并返回标签与可视化说明。"""
    if not (text or "").strip():
        return "—", "请输入待分类的治理相关文本（如公司治理、ESG 披露等）。"
    lines = [
        "[演示] 已对输入文本进行治理分类（未加载真实模型）。",
        "分类结果示例（占位）：",
        "  类别：治理相关 (governance) — 置信度: 0.xx",
        "  类别：非治理 — 置信度: 0.xx",
        "",
        "加载真实 GovernanceBERT-governance 后，将在此显示实际分类标签与置信度。",
    ]
    return "治理相关（演示）", "\n".join(lines)


def build_ui():
    with gr.Blocks(title="GovernanceBERT-governance 文本分类 WebUI") as demo:
        gr.Markdown("## GovernanceBERT-governance · 治理文本分类 WebUI 演示")
        gr.Markdown(
            "本界面以交互方式展示 GovernanceBERT-governance 在 ESG 治理领域文本分类中的典型使用流程，"
            "包括模型加载状态与分类结果的可视化展示。"
        )

        with gr.Row():
            load_btn = gr.Button("加载模型（演示）", variant="primary")
            status_box = gr.Textbox(label="模型状态", value="尚未加载", interactive=False)
        load_btn.click(fn=fake_load_model, outputs=status_box)

        with gr.Tabs():
            with gr.Tab("文本分类"):
                gr.Markdown("在下方输入治理相关文本（如公司治理、董事会、ESG 披露等），模型将输出分类标签与置信度。")
                inp = gr.Textbox(
                    label="输入文本",
                    placeholder="例如：The board of directors approved the new governance policy...",
                    lines=4,
                )
                with gr.Row():
                    label_out = gr.Textbox(label="预测标签", interactive=False)
                    detail_out = gr.Textbox(label="结果说明", lines=8, interactive=False)
                run_btn = gr.Button("执行分类（演示）")
                run_btn.click(
                    fn=fake_classify,
                    inputs=inp,
                    outputs=[label_out, detail_out],
                )

        gr.Markdown(
            "---\n*说明：当前为轻量级演示界面，未实际下载与加载 GovernanceBERT-governance 模型参数。*"
        )

    return demo


def main():
    app = build_ui()
    app.launch(server_name="127.0.0.1", server_port=7860, share=False)


if __name__ == "__main__":
    main()
