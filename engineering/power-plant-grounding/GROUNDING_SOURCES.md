# 接地原理｜公開來源與證據紀錄

> 本檔為第一輪來源紀錄，保留作歷史參照。「缺少獨立機構來源」等狀態已由後續工作更新；請以 [v1.0 查證紀錄](GROUNDING_EVIDENCE.md) 為準。

查核日期：2026-10-31。此清單區分已讀公開原文與僅查核目錄的標準；不代表已完成臺灣法規或特定電廠適用性審查。

## 已核對、供初稿引用的公開原文

| ID | 發布機構、文件與連結 | 已核對位置 | 支持內容與使用界線 |
| --- | --- | --- | --- |
| S01 | 美國 OSHA：[1910.269 Appendix C — Protection From Hazardous Differences in Electric Potential](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.269AppC) | I；II.A–B；III.A–C | 接地物體的電位、地表電位梯度、步間與接觸電壓、連結與等電位區。原文為電力作業保護脈絡，不直接取代永久接地網設計標準。HTML 無固定頁碼，以段落定位。 |
| S02 | 美國 OSHA：[1910.304 — Wiring design and protection](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) | (g)(4)(i)、(g)(5)、(g)(8)(i)；另查閱 (g)(1)(v)(E) | 已接地系統的導體連接、接地路徑連續性；條文另有特定高阻抗接地情況。美國法規頁，不能直接宣稱為臺灣電廠法定要求。頁尾列修訂資訊至 2008 年；不把查閱日期當成發布年份。 |
| S03 | 美國 OSHA：[Construction eTool — Electrical Incidents: Grounding](https://www.osha.gov/etools/construction/electrical-incidents/grounding) | System or Service Ground、Equipment Ground；Methods of Grounding Equipment | 系統接地與設備接地的入門區分。屬營造安全教學頁，未見明確版次；不外推其接地位置、接地極數值或低壓示例至所有電廠設備。 |

這些資料均已開啟官方頁面並閱讀所列段落，並非僅使用搜尋摘要；未保存整頁副本。網頁更新後應依條款定位重新核對。

## IEEE／IEC 候選標準：尚未核對全文

| 文件 | 官方入口 | 下一步需要確認 |
| --- | --- | --- |
| IEEE 3003.1-2019 | https://standards.ieee.org/ieee/3003.1/4438/ | 中性點接地、故障回路及適用系統的全文條款 |
| IEEE 3003.2-2014 | https://standards.ieee.org/ieee/3003.2/4439/ | 設備連結、保護協調；目錄狀態 Inactive-Reserved |
| IEEE 80-2013，含 Cor 1-2015 | https://standards.ieee.org/ieee/80/4089/ | 地電位升高、接觸與步間電壓的正式定義及計算條件；目錄狀態 Inactive-Reserved |
| IEC 61936-1:2021 | https://webstore.iec.ch/en/publication/64490 | 高壓裝置接地條款與適用性 |
| IEC 60479-1:2018 | https://webstore.iec.ch/en/publication/62980 | 人體電流效應與各項假設；不從目錄推導人體容許值 |

官方目錄狀態沿用本專案同日的前次查核；以上文件均未作為本版初稿的已核實條款依據。

## 第一版內容與證據對照

| 初稿主題 | 依據 | 證據層次 |
| --- | --- | --- |
| 系統接地／設備接地的問題區分 | S03 | 公開教材的概念摘要 |
| 故障回路示意 | S02 (g)(4)(i)、(g)(8)(i) | 依已接地系統連接關係自行整理；不是標準原圖 |
| 接地不等於零電位 | S01 I、II.A | 原文原理摘要 |
| 步間與接觸電壓 | S01 II.B | 原文定性說明，不提供設計限值 |
| 連結與等電位區 | S01 III.A、III.C.1 | 原文概念摘要，不延伸為施工指示 |
| 單一接地電阻不足以判定安全 | S01 I、III.B，S02 (g)(5) | 本報告綜合推論，非引用的標準原句 |

## 研究缺口

- 接地電阻與頻率相關阻抗的完整解釋，尚待補強公開技術教材。
- 發電機中性點、廠用系統與開關場的差異尚未展開。
- 暫態、防雷與儀表接地本版不涵蓋。
- 尚未有第二個獨立機構的已核對全文對主要原理做交叉覆核；目前三份公開正文均來自 OSHA。
- 無電廠圖說、系統電壓及保護設定；不得從本稿推出現場設計結論。
- 曾搜尋到 USBR 維護文件與 UFC 資料，但未完成相關全文查核，未列入初稿證據。
