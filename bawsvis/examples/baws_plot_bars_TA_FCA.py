#!/usr/bin/env python3
# Copyright (c) 2020 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2021-11-08 12:22

@author: johannes
"""
import numpy as np
import pandas as pd
from scipy import interpolate
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import dates

sns.set(style="ticks", palette="pastel")
# sns.set(style="darkgrid")
# sns.set(style="whitegrid")


def change_width(ax, new_value):
    for patch in ax.patches:
        current_width = patch.get_width()
        diff = current_width - new_value
        patch.set_width(new_value)
        patch.set_x(patch.get_x() + diff * .5)


if __name__ == "__main__":
    df = pd.read_excel(
        r'C:\Temp\baws_reanalys\annual_stats_norm.xlsx',
        sheet_name='data',
    )
    df_monthly = pd.DataFrame({
        'year': df['year'].to_list() * 3,
        'fca': df['june'].to_list() + df['july'].to_list() + df['august'].to_list(),
        'month': ['Juni'] * df['year'].__len__() + ['Juli'] * df['year'].__len__() + ['Augusti'] * df['year'].__len__()
    })
    df_monthly['fca'] = df_monthly['fca'] * 100
    df['median_period_[june-20_sep-01]'] = df['median_period_[june-20_sep-01]'] * 100

    df['total_area'] = df['total_area'] / 1000.

    label_mapper = {
        'total_area': 'Total area (1000 km$^{2}$)',
        'median_period_[june-20_sep-01]': 'FCA (%)',
        'monthly': 'FCA (%)',
        # 'june': 'FCA - Juni',
        # 'july': 'FCA - Juli',
        # 'august': 'FCA - Augusti',
    }
    fig, axes = plt.subplots(3, 1, figsize=(8, 8), sharex=True)
    for ax, data_key, note in zip(axes, ('total_area', 'median_period_[june-20_sep-01]', 'monthly'),
                                  ('a', 'b', 'c')):
        if data_key == 'monthly':
            sns.barplot(x=df_monthly['year'], y=df_monthly['fca'],
                        # color='gray',
                        hue=df_monthly['month'],
                        ax=ax)
            ax.legend(title='', frameon=False, loc='upper left')
        else:
            sns.barplot(x=df['year'], y=df[data_key],
                        color='gray',
                        ax=ax)
            change_width(ax, .5)
        sns.despine(offset=5, ax=ax, fig=fig)
        # if data_key == 'total_area':
        #     ax.ticklabel_format(axis='y', style='sci', scilimits=(1, 2), useMathText=True)
        ax.set_ylabel(label_mapper.get(data_key))
        ax.set_xlabel('')

        y_text_pos = ax.get_ylim()[1] - (ax.get_ylim()[1] - ax.get_ylim()[0]) / 9.
        ax.text(ax.get_xlim()[-1], y_text_pos, note)

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('TA_FCA_2022_v2.png', dpi=600)
