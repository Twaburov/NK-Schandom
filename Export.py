from Objects import *


def export_all(filename):
    import openpyxl
    wb = openpyxl.load_workbook(filename)
    wb.remove(wb['Pairing'])
    print_pairing(wb.create_sheet('Pairing'))
    wb.save(filename)


def print_pairing(ws):
    rownr = 1

    for r in Round.rounds:
        matchnr = 0
        for m in r.matches:
            ws.cell(row=rownr, column=1, value=str(r.round_nr) + chr(65 + matchnr))  # e.g: 1A, 3F, 5D
            ws.cell(row=rownr, column=2, value=Player.player_dict[m.p1nr].name)
            ws.cell(row=rownr, column=3, value=Player.player_dict[m.p2nr].name)
            if m.Game != None:
                p1 = get_player_by_pairing_number(m.p1nr)
                p2 = get_player_by_pairing_number(m.p2nr)
                ws.cell(row=rownr, column=6, value=m.Game.name)
                ws.cell(row=rownr, column=7, value=get_player_weight_for_game(p1, m.Game, p2))
                ws.cell(row=rownr, column=8, value=get_player_weight_for_game(p2, m.Game, p1))
            rownr += 1
            matchnr += 1
