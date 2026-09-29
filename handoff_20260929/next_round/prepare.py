"""Prepare TG-target tasks from frozen evidence. No retrieval, training or labeling."""
import copy
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent


def write(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def main():
    subprocess.run([sys.executable, str(ROOT / 'cleaned_ite_tg/verify.py')], check=True)
    needs = json.loads((ROOT / 'kg_tg_driven_crossmap_20260929/tg_needs.json').read_text())
    hypotheses = json.loads((ROOT / 'kg_tg_driven_crossmap_20260929/hypotheses.json').read_text())
    splits = {
        'N01': [('N01', '红氧物种在凝胶中的有效传输', 'Improve redox-species mass transport in a TG gel while retaining electrochemical accessibility.')],
        'N02': [('N02', '配对与解离对浓度梯度的影响', 'Reduce detrimental ion pairing in the specified TG electrolyte; verify free species and concentration gradients.')],
        'N03': [('N03a', 'TG 凝胶失水与水分维持', 'Maintain water content and redox electrolyte concentration during loaded TG operation.'),
                ('N03b', 'TG 凝胶冻结与低温运行', 'Resist freezing while maintaining redox-species mobility and TG output at low temperature.')],
        'N04': [('N04a', 'TG 电极界面反应动力学', 'Improve redox charge-transfer kinetics in the specified TG electrolyte.'),
                ('N04b', 'TG 电极长期化学与运行稳定性', 'Maintain TG electrode function against dissolution and passivation during sustained operation.')],
    }
    tasks = []
    for need in needs:
        assert need['anchor'].startswith('TG:')
        assert all(cid.startswith('TG:') for cid in need['known'])
        for task_id, title, objective in splits[need['id']]:
            task = copy.deepcopy(need)
            task.update(id=task_id, parent_need=need['id'], title=title,
                        query=objective, outcome=objective,
                        knowledge_source_domain='iTE', application_domain='TG',
                        evaluation_domain='TG', status='proposed_not_retrieved',
                        known_evidence_scope='Inherited parent context; relevance to this subneed requires review.')
            tasks.append(task)
    queue = []
    for hyp in hypotheses:
        assert hyp['source'] and all(x.startswith('iTE:') for x in hyp['source'])
        assert hyp['target'] and all(x.startswith('TG:') for x in hyp['target'])
        queue.append({key: hyp[key] for key in ['id', 'title', 'status', 'source', 'target', 'mechanism', 'hypothesis', 'existing', 'gap', 'validation']})
        queue[-1].update(application_domain='TG', evidence_status='abstract_supported_source_hypothesis_not_TG_validation',
                         full_text_review='pending', external_TG_prior_art_review='pending', experiment='not_run')
    write('atomic_tg_needs.json', tasks)
    write('hypothesis_validation_queue.json', queue)
    write('preparation_verification.json', {
        'status': 'PASS', 'source_needs': len(needs), 'atomic_needs': len(tasks),
        'hypotheses': len(queue), 'target_domain': 'TG', 'knowledge_source': 'iTE',
        'new_retrieval_or_training': False, 'scientific_transfer_validated': False,
    })
    print('PASS: 6 TG-target tasks and 3 hypothesis validation cards; no new performance claims.')


if __name__ == '__main__':
    main()
